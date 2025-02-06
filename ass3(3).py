def length(n):
    result=1
    if n is 0:
        print("1")
    else:
        for i in range(0,n):
            if(i%2==0):
                result=result*2;
            else:
                result=result+1;
        print(result)
t=int(input("enter no of test cases"))
print("enter no of cycles");
for i in range(0,t):
    n=int(input())
    length(n)
