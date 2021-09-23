def bubbleSort(list1):
    for passnum in range(len(list1) - 1, 0, -1):
        for i in range(passnum):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
            else:
                continue

list1 = [54,26,93,17,77,31,44,55,20]
bubbleSort(list1)
print(list1)