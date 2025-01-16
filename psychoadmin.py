n=input("Enter number of employees")
n=int(n)
a=[]
for i in range(n):
    element=int(input("enter the element{i+1}:"))
    a.append(element)
print("List:",a)
swap=0   
for i in range(n):
    min=a[i]
    k=i
    for j in range(i+1,n):
        if a[j]<min:
            min=a[j]
            k=j
    if a[i]!=a[k]:
        temp=a[i]
        a[i]=a[k]
        a[k]=temp
        swap+=1
print(a)
print("Minimum swaps=",swap)
