# Write a function that rotates a list by k elements. 
# For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. 
# Try solving this without creating a copy of the list. 
# How many swap or move operations do you need?

def rotate(list1, num_input):
    while True:
        if num_input in list1:
            for i in range(0, list1.index(num_input) + 1):
                hold = list1.pop(0)
                list1.append(hold)
            break
        else:
            print("Please enter a number from the list")
    return list1
        


list1 = [1, 2, 3, 4, 5, 6, 7]
print("Here's the list: ", list1)
user_input = int(input("Enter a number from the list to rotate it by: "))
print("Here's your swerved list: ", rotate(list1, user_input))




