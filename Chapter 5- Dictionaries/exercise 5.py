pets = []


pet = {
    'animal type': 'python',
    'name': 'viperion',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'duck',
    'name': 'rocky',
    'owner': 'sagar alias',
    'weight': 3,
    'eats': 'worms',
}
pets.append(pet)

pet = {
    'animal type': 'goat',
    'name': 'salman khan',
    'owner': 'sharukh khan',
    'weight': 31,
    'eats': 'leaves',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")