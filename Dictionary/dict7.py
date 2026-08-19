# Write a Python function named merge_dicts(d1, d2) that accepts two
# dictionaries (d1 and d2) as arguments and returns a new dictionary
# formed by merging them using the update() method. Ensure d1 remains
# unchanged

dict1 = {
    "name": "Luna",
    "age": 19,
    "city": "Balasore"
}

dict2 = {
    "course": "B.Tech",
    "branch": "CSE",
    "year": 1
}


def merge_dicts(d1, d2):
    new_dictionary = {}
    new_dictionary.update(d1)
    new_dictionary.update(d2)
    return new_dictionary

a = merge_dicts(dict1,dict2)
print(a)
print(dict1)
print(dict2)