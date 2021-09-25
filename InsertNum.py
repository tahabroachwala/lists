def insertNumInList(list1, num, index_to_insert_at):
    list1.append(num)
    if index_to_insert_at > len(list1):
        print("The index you've entered is out of bounds for this list.")
    index_count = len(list1) - 1
    while index_count != index_to_insert_at:
        list1[index_count], list1[index_count-1] = list1[index_count-1], list1[index_count]
        index_count -= 1
    return list1

list1 = [2, 3, 4, 6, 7, 8, 9]
num_input = int(input("Enter the number you want to insert into the list: "))
index_input = int(input("Enter the index where you want to place the new number: "))
print(insertNumInList(list1, num_input, index_input))
