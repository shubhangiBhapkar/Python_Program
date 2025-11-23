# u are given list of programming language
# ["python","java","c++","python","java","c"]
# Convert it into a set and print how many unique languages Divya knows

programming = ["python","java","c++","python","java","c"]
print(type(programming))
# how to convert list into set
progSet = set(programming)
print(type(progSet))
print(programming)
print(progSet)
print("Divya knows these many languages: ",len(progSet))