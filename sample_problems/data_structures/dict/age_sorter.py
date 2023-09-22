# age_sorter.py

def sort_ages_in_dict(people_dict):
    sorted_people_dict = {}

    # Find the minimum age in the dictionary
    while people_dict:
        min_age = min(people_dict.values())

        # Find the corresponding name for the minimum age
        for name, age in people_dict.items():
            if age == min_age:
                sorted_people_dict[name] = min_age
                del people_dict[name]
                break  # Move to the next age

    return sorted_people_dict
