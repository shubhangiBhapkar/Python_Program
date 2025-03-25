# #problem 1
str1=input("Enter a string : ")
str2=input("Enter a string : ")
if str2 in str1 :
    print(f"{str2} in {str1} : True")
else:
    print(f"{str2} in {str1} : False")

#problem 2

s="c@mm*u^ication"
a=input("enter charactre : ")
b=input("enter charactre : ")
c=input("enter charactre : ")
if a in s:
    if b in s:
        if c in s:
            print("True")
else:
    print("False")
