# Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]

def conc(list1, list2):
    list1.extend(list2)
    return list1

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(conc(list1, list2))