def switch_dict_keys_and_values(d):
    return {v: k for k, v in d.items()}

d = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

new_d = switch_dict_keys_and_values(d)
print(new_d)