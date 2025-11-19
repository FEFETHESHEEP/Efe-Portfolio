import os
import asyncio
import time
from collections import defaultdict, deque

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("1404504761897849053"))
MOD_LOG_CHANNEL_ID = int(os.getenv("1404504762841301103"))

# ---------- Settings ----------
JOIN_WINDOW_SECONDS = 15
JOIN_BURST_THRESHOLD = 6
LOCKDOWN_DURATION = 300
USER_MSG_WINDOW = 6
USER_MSG_THRESHOLD = 10
MENTION_THRESHOLD = 8
MUTE_DURATION = 600

EXEMPT_CHANNEL_IDS = set("👷🏻‍moderator-chat💬")  

# ---------- Bot ----------
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

join_times = deque(maxlen=200)
user_msg_times = defaultdict(lambda: deque())
lockdown_on = False
lockdown_until = 0

async def get_mod_log_channel(guild: discord.Guild):
    if MOD_LOG_CHANNEL_ID: ("1404504762841301103")
        ch = guild.get_channel(MOD_LOG_CHANNEL_ID)
        if isinstance(ch, discord.TextChannel):
            return ch
    for ch in guild.text_channels:
        if ch.name.lower() in ("mod-log", "logs"):
            return ch
    return None

async def log(guild: discord.Guild, text: str):
    ch = await get_mod_log_channel(guild)
    if ch: ("1404504762841301103")
        await ch.send(text)

async def find_or_create_muted_role(guild: discord.Guild):
    muted = discord.utils.get(guild.roles, name="Muted")
    if muted is None:
        muted = await guild.create_role(name="Muted", reason="For auto-muting spam")
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
    reason = "Raid detected" if enabled else "Lockdown ended"
    await log(guild, f"🔒 Lockdown {'ON' if enabled else 'OFF'} — {reason}")

    everyone = guild.default_role
    for channel in guild.text_channels:
        if channel.id in EXEMPT_CHANNEL_IDS:
            continue
        try:
            overwrite = channel.overwrites_for(everyone)
            overwrite.send_messages = None if not enabled else False
            await channel.set_permissions(everyone, overwrite=overwrite)
        except Exception:
            pass

    if enabled:
        lockdown_until = int(time.time()) + LOCKDOWN_DURATION

@tasks.loop(seconds=5)
async def lockdown_watchdog():
    global lockdown_on, lockdown_until
    if lockdown_on and time.time() >= lockdown_until:
        for guild in bot.guilds:
            await set_lockdown(guild, False)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    lockdown_watchdog.start()

@bot.event
async def on_member_join(member):
    if GUILD_ID and member.guild.id != GUILD_ID:
        return
    now = time.time()
    join_times.append(now)
    while join_times and (now - join_times[0]) > JOIN_WINDOW_SECONDS:
        join_times.popleft()
    if len(join_times) >= JOIN_BURST_THRESHOLD and not lockdown_on:
        await log(member.guild, f"🚨 Raid detected ({len(join_times)} joins/{JOIN_WINDOW_SECONDS}s). Enabling lockdown.")
        await set_lockdown(member.guild, True)

@bot.event
async def on_message(message):
    if not message.guild or message.author.bot:
        return
    now = time.time()
    dq = user_msg_times[message.author.id]
    dq.append(now)
    while dq and (now - dq[0]) > USER_MSG_WINDOW:
        dq.popleft()
    mention_count = len(message.mentions) + message.content.count("@everyone") + message.content.count("@here")
    if mention_count >= MENTION_THRESHOLD or len(dq) >= USER_MSG_THRESHOLD:
        muted = await find_or_create_muted_role(message.guild)
        await message.author.add_roles(muted, reason="Auto-mute: spam")
        await log(message.guild, f"🔇 Auto-muted {message.author.mention} for {MUTE_DURATION}s")
        async def unmute_later(user):
            await asyncio.sleep(MUTE_DURATION)
            try:
                await user.remove_roles(muted, reason="Unmute after timeout")
                await log(message.guild, f"🔊 Unmuted {user.mention}")
            except Exception:
                pass
        bot.loop.create_task(unmute_later(message.author))
    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def lockdown(ctx):
    await set_lockdown(ctx.guild, True)
    await ctx.send("🔒 Lockdown enabled.")

@bot.command()
@commands.has_permissions(manage_guild=True)
async def unlock(ctx):
    await set_lockdown(ctx.guild, False)
    await ctx.send("🔓 Lockdown disabled.")

bot.run(TOKEN)
