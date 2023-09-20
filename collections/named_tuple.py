from collections import namedtuple

# Define a namedtuple named 'Person' with 'name' and 'age' fields
Person = namedtuple('Person', 'name age')

# Create an instance of Person
person = Person(name='Alice', age=30)

# Access fields using dot notation
print("Name:", person.name)
print("Age:", person.age)
