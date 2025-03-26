def Biodata():
    s="Hellow I Am Python programmer."
    print(s)

Biodata()

#Take a String from user ,create string made of first and middle char
str1=input("Enter one String: ")
if 1<=len(str1) and len(str1) <= 50:
    str2=str1[0]
    str2+=str1[int(len(str1)/2)]
    print(str2)

##

str=input("Enter one string with upper and lower case:")
for char in str :
    if char.isupper:
        str1+=char
