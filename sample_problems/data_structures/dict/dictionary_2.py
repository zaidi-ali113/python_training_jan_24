#Write a program that accepts a dictionary of people's names and their ages, and returns a new dictionary containing the same data, but with the ages sorted in ascending order.
# Please note: Order of elements added to a dictionary is maintained.

# main.py
from age_sorter import sort_ages_in_dict

# Example usage:
people_dict = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "David": 28
}

sorted_people_dict = sort_ages_in_dict(people_dict)
print(sorted_people_dict)
