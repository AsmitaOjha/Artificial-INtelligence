def likes(person, hobby):
    return (person, hobby)

# Data representing people and their hobbies
hobbies = [
    likes("John", "football"),
    likes("John", "reading books"),
    likes("Alice", "painting"),
    likes("Alice", "playing tennis"),
    likes("Bob", "football"),
    likes("Bob", "watching movies"),
    likes("Mary", "gardening"),
    likes("Mary", "reading books")
]

# Queries
print("People and Their Hobbies:")
print(hobbies)

# Find hobbies that John and mary both like
john_hobbies = set(hobby for (person, hobby) in hobbies if person == "John")
mary_hobbies = set(hobby for (person, hobby) in hobbies if person == "Mary")
common_hobbies = john_hobbies.intersection(mary_hobbies)
print("Hobbies that both John and Mary like:", common_hobbies)

# Find people who like football
people_who_like_football = [person for (person, hobby) in hobbies if hobby == "football"]
print("People who like football:", people_who_like_football)
