import random

tech_words = ["AI-powered", "blockchain-based", "quantum-enhanced", "IoT-enabled", "metaverse-ready"]
objects = ["toaster", "umbrella", "backpack", "mirror", "coffee mug"]
target_markets = ["for pets", "for gamers", "for seniors", "for digital nomads", "for toddlers"]

def generate_startup_idea():
    tech = random.choice(tech_words)
    obj = random.choice(objects)
    market = random.choice(target_markets)
    return f"A {tech} {obj} {market}"

# Generate 5 random startup ideas
for _ in range(5):
    print(generate_startup_idea())

    print("tanny was here")
    print("Art was here")
    print("Big was here")