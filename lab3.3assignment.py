dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)
merged_dict2 = {**dict1, **dict2}
print(merged_dict2)
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(dict1_copy)