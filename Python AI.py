print("Hi there! What's your name?")
name = input()
print(f"Nice to meet you, {name}!")

print("Just a few fun questions to get to know you better 😊")

print("What's your favorite color?")
color = input()
print(f"{color} is such a great color!")

print("What's your favorite food?")
food = input()
print(f"Yum! I love {food} too.")

print("Do you have a favorite animal?")
animal = input()
print(f"{animal}s are amazing!")

print("How about a hobby? What do you enjoy doing?")
hobby = input()
print(f"That sounds like a lot of fun! I'd love to try {hobby} someday.")

print("What's your favorite sport?")
sport = input()
print(f"{sport} is a really exciting sport!")

print("What's your favorite subject in school?")
subject = input()
print(f"{subject} can be super interesting!")

print("Do you have a favorite book?")
book = input()
print(f"{book} sounds like a great read!")

print("How about a favorite movie?")
movie = input()
print(f"{movie}? Classic choice!")

print("Do you watch any TV shows? What's your favorite?")
tvshow = input()
print(f"I've heard good things about {tvshow}!")

print("What’s your favorite song?")
song = input()
print(f"{song} is such a catchy tune!")

print("Do you have a favorite game?")
game = input()
print(f"{game} is awesome—I like that one too!")

print("Do you play any musical instruments? (yes or no)")
play_instruments = input().strip().lower()

if play_instruments == "yes":
    print("Cool! What instrument(s) do you play?")
    instruments = input()
    print(f"Nice! I play the drums, but {instruments} sounds awesome too!")
else:
    print("You should give it a try sometime—playing music is a great way to relax and express yourself 🎶")

print("\nThanks for sharing all that, " + name + "! It was great learning more about you 😄")

print("\nA few more fun questions...")

print("Do you prefer summer or winter?")
season = input()
print(f"{season.capitalize()} is a great choice!")

print("Do you like the beach or the mountains more?")
landscape = input()
print(f"Nice! {landscape} can be so peaceful.")

print("Are you more of a morning person or a night owl?")
personality = input()
print(f"Ah, a {personality}! I'm the same.")

print("What's a dream place you'd love to visit?")
travel = input()
print(f"{travel} sounds amazing! Hope you get to go there someday.")

print("What do you want to be when you grow up?")
dream_job = input()
print(f"{dream_job} is such an inspiring goal!")

print("If you could have any superpower, what would it be?")
superpower = input()
print(f"{superpower.capitalize()} would be incredible to have!")

# Summary
print("\n🎉 Thanks for sharing so much, " + name + "! Here's what I've learned about you:")

print(f"🌈 Favorite color: {color}")
print(f"🍔 Favorite food: {food}")
print(f"🐾 Favorite animal: {animal}")
print(f"🎨 Favorite hobby: {hobby}")
print(f"⚽ Favorite sport: {sport}")
print(f"📚 Favorite subject: {subject}")
print(f"📖 Favorite book: {book}")
print(f"🎬 Favorite movie: {movie}")
print(f"📺 Favorite TV show: {tvshow}")
print(f"🎵 Favorite song: {song}")
print(f"🎮 Favorite game: {game}")

if play_instruments == "yes":
    print(f"🎹 Instruments you play: {instruments}")
else:
    print("🎹 You don't play an instrument (yet!)")

print(f"🌤️ Preferred season: {season}")
print(f"🏞️ Beach or mountains: {landscape}")
print(f"🕰️ You're a: {personality}")
print(f"✈️ Dream travel destination: {travel}")
print(f"💼 Dream job: {dream_job}")
print(f"🦸 Superpower you'd love to have: {superpower}")

print("\nIt was so great chatting with you, " + name + "! Hope you have a fantastic day! 😄")

print ("Goodbye!👋")