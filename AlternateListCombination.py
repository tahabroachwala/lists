# Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

def combine(list1, list2):
    empty = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            empty.append(list1[i])
            empty.append(list2[i])
    return empty

list1 = ["a","b","c"]
list2 = [1,2,3]
print(combine(list1, list2))
