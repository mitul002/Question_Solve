list1 = [1, 4, 6, 8, 9]
list2 = [2, 5, 7]

set1=set(list1)
set2=set(list2)

# Find the common elements between list1 and list2
common_elements = set1 & set2

if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements found.")