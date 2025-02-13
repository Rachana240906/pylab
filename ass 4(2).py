a=[]
for i in range(100):
    a.append(i*i)
m=int(input("enter first number"))
n=int(input("enter last number"))
b=[]
for i in range(m,n):
    b.append(i)
common=list(set(a)&set(b))
common.sort()
print(common)
