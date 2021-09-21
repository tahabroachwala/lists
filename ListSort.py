# Write a function that merges two sorted lists into a new sorted list. 
# [1,4,6],[2,3,5] → [1,2,3,4,5,6]. 
# You can do this quicker than concatenating them followed by a sort.

def conc(list1, list2):
    list3 = sorted(list1 + list2)
    return list3

list1 = [1,4,6]
list2 = [2,3,5]
print(conc(list1, list2))