def droot(n):
    newn=0
    p=n
    if p>9:
     while n>0:
        q=n%10
        newn=newn+q
        n=n//10
    print(newn)
n=int(input("enter any number"))
droot(n)
