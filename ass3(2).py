fibo=[0,1]
c=0
n=int(input("enter any number"))
a=0
b=1
nt=a+b
while nt<=n:
    fibo.append(nt)
    a=b
    b=nt
    nt=a+b
print(fibo)
testnum=[]
t=int(input("enter the no.of test cases"))
for i in range(0,t):
    n=int(input("enter the numbers to be tested"))
    testnum.append(n)
    print(testnum)
for i in range(0,t):
    for j in range(0,t):
        if (testnum[i]==fibo[j]):
            c=1
    if c==1:
        print("IsFibo")
    else:
        print("IsNotFibo")       
