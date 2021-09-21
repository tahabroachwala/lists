# Write a function that computes the list of the first 100 Fibonacci numbers. 
# The first two Fibonacci numbers are 1 and 1. 
# The n+1-st Fibonacci number can be computed by adding the n-th and the n-1-th Fibonacci number. 
# The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.

import math

def fibonacci():
    count = 0
    n1, n2 = 0, 1
    list1 = []
    while count < 101:
        list1.append(n1)
        fib = n1 + n2
        n1 = n2
        n2 = fib
        count += 1
    return list1

print(fibonacci())