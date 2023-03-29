def sublist_second_ele(lst, start, end):
    sub_list = lst[start: end+1]
    return sub_list[0::2]

lst = [2,3,5,7,11,13,17,19,23,29,31,37,41]
start = 2
end = 9

sub_lst = sublist_second_ele(lst, start, end)

print(sub_lst)