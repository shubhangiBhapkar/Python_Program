n=int(input())
m=int(input())
for i in range(n,m):
    if i % 5 == 0:
        break
print(i)

#continue
for num in range(1,20):
    if num <=10 :
        continue
    print(num)