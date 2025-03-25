num=int(input("Enter a two digit positive number :"))
l_digit=num % 10
f_digit=num // 10
product=l_digit*f_digit
if product < 50 :
    print(f" number itself : {num}")
else:
    print("Invalid")