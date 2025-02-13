def lettercheck(a):
    n=len(a)
    h=n-1
    i=0
    c=0 
    while i<n//2:
        if a[i]==a[h]:
            h=h-1
            i=i+1
        else:
            c += abs(ord(a[i]) - ord(a[h]))
            i=i+1
            h=h-1
        #print(c)
    return c
def cpalindrome(a):
    b=a[::-1]
    c = 0
    if a==b:
        print("it is palindrome")
    else:
        c = lettercheck(a)
    return c

t=int(input("enter the no of test cases"))
for i in range(t):
    a=input("enter the string")
    print(cpalindrome(a))
