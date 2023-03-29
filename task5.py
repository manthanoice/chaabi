def compare_lists(list1, list2):
    common = set(list1).intersection(list2)
    symmetric_difference = set(list1).symmetric_difference(list2)
    return list(common), list(symmetric_difference)
    
mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

common_elements, symmetric_difference = compare_lists(mainstream, must_watch)

print("Common Elements: ", common_elements)
print("Symmetric Difference: ", symmetric_difference)