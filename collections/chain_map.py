from collections import ChainMap

# Create dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Create a ChainMap
chain_map = ChainMap(dict1, dict2)

# Access values
value_a = chain_map['a']  # Gets from dict1
value_b = chain_map['b']  # Gets from dict1 (overrides dict2)
value_c = chain_map['c']  # Gets from dict2

x=1