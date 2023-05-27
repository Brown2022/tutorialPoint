#!/usr/bin/python3

Number = int(input("Enter the fibonacci number of range 50:"))

n1 = 0
n2 = 1
sum  = 0

for Num in range(0, Number):
    print(n1, end = ' ')
    sum = sum + n1
    next = n1 + n2
    n1 = n2
    n2 = next

print("\nSum of the First Fifty Fibonacci Series Nummbers: %d" %sum)
