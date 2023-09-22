#Write a program that takes a list of numbers and a set of numbers.
# For each number in the list, check if it exists in the set,
# and return a new set containing only those numbers that exist in both the list and the set.

# main.py
from common_elements import common_elements_in_list_and_set

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
numbers_set = {3, 4, 5, 6, 7}
result = common_elements_in_list_and_set(numbers_list, numbers_set)
print(result)
