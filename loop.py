# temp=[10,20,30,40,50]
# for day in temp:
#     print(day, end =' ')

# city="Sangamner"
# for char in city: 
#     print(char)

# #length
# length=0
# for i in "Hellow good morning":
#     length+=1
# print(f"Length of sequence is :  {length}")

# #sum of temp
# sum=0
# for day in temp:
#     sum+=day
# print(f"Sum of temperatures :{sum}")

# ##Avearge of temp
# sum=0
# length=0
# for day in temp:
#     sum+=day
#     length+=day
# print(f"{sum /length:.2f}")

# #factors
# num=int(input("enter integer"))
# for i in range(1, num):
#     #print(i)
#     if num % i==0:
#         print(i)

# #even Numbers In range
# for n in range(0,15,2):
#     print(n)

#addition of first n natural number enter by user
sum=0
num=int(input("Enter natural number :"))
for i in range(0,num):
    sum+=i
print(f"Addition of numbers upto {num} is {sum}")

#even number adition
sum=0
for i in range(0,num,2):
    sum+=i
print(f"Even number addition between 1 to {num } is :{sum} ")
#odd number
sum=0
for i in range(0,num,3):
    sum+=i
print(f"Even number addition between 1 to {num } is :{sum} ")

    