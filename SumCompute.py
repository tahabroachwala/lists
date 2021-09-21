def usingForLoop(list1):
    summation = 0
    for i in list1:
        summation += i
    return summation

def usingWhileLoop(list1):
    j = 0
    summation_2 = 0
    while j < len(list1):
       summation_2 += list1[j] 
       j += 1
    return summation_2

list1 = [10, 34, 56, 90, 12, 34, 45, 56, 78]
print("Using For Loop:", usingForLoop(list1))
print("Using While Loop:", usingWhileLoop(list1))

