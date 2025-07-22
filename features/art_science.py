import random

def get_random_art():
    # Just sample placeholder art (ASCII or names of artworks)
    art_list = [
        "The Starry Night – Vincent van Gogh",
        "The Persistence of Memory – Salvador Dalí",
        "Girl with a Pearl Earring – Johannes Vermeer",
        "Mona Lisa – Leonardo da Vinci",
        "The Great Wave off Kanagawa – Hokusai"
    ]
    return random.choice(art_list)

def get_science_fact():
    # Fun science facts
    facts = [
        "Water can boil and freeze at the same time.",
        "Bananas are radioactive.",
        "Octopuses have three hearts.",
        "Humans share 60% of their DNA with bananas.",
        "The Eiffel Tower can be 15 cm taller in the summer."
    ]
    return random.choice(facts)