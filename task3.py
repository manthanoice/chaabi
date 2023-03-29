def sort_list_of_dicts(lst, key):
    def get_dict_key(item):
        return item[key]
    return sorted(lst, key=get_dict_key)

lst = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_lst = sort_list_of_dicts(lst, "fruit")
print(sorted_lst)