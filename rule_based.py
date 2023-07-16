def is_carnivore_animal(animal):
    carnivores = ['lion', 'tiger', 'leopard', 'cheetah']
    return animal.lower() in carnivores

def is_herbivore_animal(animal):
    herbivores = ['elephant', 'giraffe', 'deer', 'rhinoceros']
    return animal.lower() in herbivores

def classify_animal_diet(animal):
    if is_carnivore_animal(animal):
        return "Carnivore"
    elif is_herbivore_animal(animal):
        return "Herbivore"
    else:
        return "Unknown"

# Usage example:
animal_name = "giraffe"
print(f"{animal_name} is a {classify_animal_diet(animal_name)}.")
