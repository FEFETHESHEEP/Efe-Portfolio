import os
import asyncio
import time
from collections import defaultdict, deque

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

GUILD_ID = 1404504761897849053

MOD_LOG_CHANNEL_ID = int(os.getenv("1404504762841301103")) if os.getenv("1404504762841301103") else None
_exempt = os.getenv("1404504762841301103")
EXEMPT_CHANNEL_IDS = set(int(x.strip()) for x in _exempt.split(",") if x.strip())

JOIN_WINDOW_SECONDS = 15      
JOIN_BURST_THRESHOLD = 6   
LOCKDOWN_DURATION = 300      
USER_MSG_WINDOW = 6        
USER_MSG_THRESHOLD = 10    
MENTION_THRESHOLD = 8         
MUTE_DURATION = 600             

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

join_times = deque(maxlen=200)
user_msg_times = defaultdict(lambda: deque())
lockdown_on = False
lockdown_until = 0


async def get_mod_log_channel(guild: discord.Guild) -> discord.TextChannel | None:
    if MOD_LOG_CHANNEL_ID:
        ch = guild.get_channel(MOD_LOG_CHANNEL_ID)
        if isinstance(ch, discord.TextChannel):
            return ch
    for ch in guild.text_channels:
        if ch.name.lower() in ("mod-log", "modlog", "logs"):
            return ch
    return None


async def log(guild: discord.Guild, text: str):
    ch = await get_mod_log_channel(guild)
    if ch:
        await ch.send(text)


async def find_or_create_muted_role(guild: discord.Guild) -> discord.Role:
    muted = discord.utils.get(guild.roles, name="Muted")
    if muted is None:
        muted = await guild.create_role(name="Muted", reason="Create default muted role")
        for channel in guild.channels:
            try:
                await channel.set_permissions(muted, send_messages=False, speak=False, add_reactions=False)
            except Exception:
                pass
    return muted


async def set_lockdown(guild: discord.Guild, enabled: bool):
    global lockdown_on, lockdown_until
    if enabled == lockdown_on:
        return
    lockdown_on = enabled
    reason = "Raid burst detected" if enabled else "Lockdown ended"
    await log(guild, f"🔒 **Lockdown {'ENABLED' if enabled else 'DISABLED'}** — {reason}")

    everyone = guild.default_role
    for channel in guild.text_channels:
        if channel.id in EXEMPT_CHANNEL_IDS:
            continue
        try:
            overwrite = channel.overwrites_for(everyone)
            overwrite.send_messages = None if not enabled else False
            await channel.set_permissions(everyone, overwrite=overwrite, reason=reason)
        except Exception:
            pass

    if enabled:
        lockdown_until = int(time.time()) + LOCKDOWN_DURATION


@tasks.loop(seconds=5)
async def lockdown_watchdog():
    if not lockdown_on:
        return
    now = int(time.time())
    if now >= lockdown_until:
        for guild in bot.guilds:
            await set_lockdown(guild, False)


@bot.event
async def on_ready():
    names = ", ".join(g.name for g in bot.guilds)
    print(f"✅ Logged in as {bot.user} — connected to: {names}")
    lockdown_watchdog.start()


@bot.event
async def on_member_join(member: discord.Member):
    if GUILD_ID and member.guild.id != GUILD_ID:
        return

    now = time.time()
    join_times.append(now)

    while join_times and (now - join_times[0]) > JOIN_WINDOW_SECONDS:
        join_times.popleft()

    if len(join_times) >= JOIN_BURST_THRESHOLD and not lockdown_on:
        await log(member.guild, f"🚨 Join burst detected ({len(join_times)} joins/{JOIN_WINDOW_SECONDS}s). Enabling lockdown.")
        await set_lockdown(member.guild, True)


@bot.event
async def on_message(message: discord.Message):
    if not message.guild or message.author.bot:
        return

    now = time.time()
    dq = user_msg_times[message.author.id]
    dq.append(now)
    while dq and (now - dq[0]) > USER_MSG_WINDOW:
        dq.popleft()

    mention_count = len(message.mentions) + message.content.count("@everyone") + message.content.count("@here")

    try:
        if mention_count >= MENTION_THRESHOLD or len(dq) >= USER_MSG_THRESHOLD:
            muted = await find_or_create_muted_role(message.guild)
            await message.author.add_roles(muted, reason="Auto-mute: spam/mention spam")
            await log(message.guild, f"🔇 Auto-muted {message.author.mention} for {MUTE_DURATION}s "
                                      f"(msgs in {USER_MSG_WINDOW}s: {len(dq)}, mentions: {mention_count}).")

            async def unmute_later(user: discord.Member):
                await asyncio.sleep(MUTE_DURATION)
                try:
                    await user.remove_roles(muted, reason="Auto-unmute after timeout")
                    await log(message.guild, f"🔊 Auto-unmuted {user.mention}.")
                except Exception:
                    pass
            bot.loop.create_task(unmute_later(message.author))
    except discord.Forbidden:
        await log(message.guild, f"⚠️ Lacking permissions to mute {message.author.mention}.")
    except Exception as e:
        await log(message.guild, f"⚠️ Error handling spam for {message.author.mention}: {e}")

    await bot.process_commands(message)


def admin_only():
    async def predicate(ctx: commands.Context):
        return ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administrator
    return commands.check(predicate)


@bot.command(name="lockdown")
@admin_only()
async def cmd_lockdown(ctx: commands.Context):
    await set_lockdown(ctx.guild, True)
    await ctx.reply("🔒 Lockdown enabled.", mention_author=False)


@bot.command(name="unlock")
@admin_only()
async def cmd_unlock(ctx: commands.Context):
    await set_lockdown(ctx.guild, False)
    await ctx.reply("🔓 Lockdown disabled.", mention_author=False)


@bot.command(name="purgejoins")
@admin_only()
async def cmd_purgejoins(ctx: commands.Context):
    join_times.clear()
    await ctx.reply("🧹 Cleared recent join counters.", mention_author=False)


@bot.command(name="settings")
@admin_only()
async def cmd_settings(ctx: commands.Context):
    msg = (
        f"**Current settings**\n"
        f"- Join burst: {JOIN_BURST_THRESHOLD} joins / {JOIN_WINDOW_SECONDS}s → lockdown {LOCKDOWN_DURATION}s\n"
        f"- Spam: {USER_MSG_THRESHOLD} msgs / {USER_MSG_WINDOW}s → mute {MUTE_DURATION}s\n"
        f"- Mention spam: ≥{MENTION_THRESHOLD} mentions → mute\n"
    )
    await ctx.reply(msg, mention_author=False)


bot.run(TOKEN)
