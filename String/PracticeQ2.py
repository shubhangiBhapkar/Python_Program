# Write a program to take food name as input and prints: middle 3 char and last 2 char
str = input("Enter food name : ")
mid = len(str)//2
print(str[mid-1:mid+2])
print(str[-2:])