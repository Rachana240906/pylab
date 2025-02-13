a=int(input("enter the first number"))
b=int(input("enter the last number"))
n=[]
for i in range(a,b):
    q=(i)^(i+1)
    n.append(q)
print(max(n))
