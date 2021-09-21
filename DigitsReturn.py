# Write a function that takes a number and returns a list of its digits. 
# So for 2342 it should return [2,3,4,2].

def returnDigits(num):
    num_string = str(num)
    num_list = [int(i) for i in num_string]
    return num_list
print(returnDigits(2432))
