# common_elements.py

def common_elements_in_list_and_set(numbers_list, numbers_set):
    common_elements = set(numbers_list) & numbers_set
    return common_elements
