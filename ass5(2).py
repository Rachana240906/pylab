t=int(input("no.of test cases"))
c=0
for i in range(t):
    n=int(input("enter no of cuts"))
    for j in range(n+1):
        q=j//2
        c=c+q
print(c)
