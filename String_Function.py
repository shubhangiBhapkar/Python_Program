char= input("Enter the String : ")
if char.isdigit():
    print(f"The char is digit")
elif char.isalpha():
    print(f"The char is alphabet")
else:
    print(f"The char is neither digit nor alphabet")