import string
a=list(string.ascii_lowercase)
a1=set(a)
print(a1)
#b=list(string.ascii_uppercase)
#print(b)
#a.append(b)
#print(a)
s=(input("enter the sentence"))
s1=set(s)
s1.remove(' ')
print(s1)
#s2=set(s1)
#print(s2)
#common=list(set(a1)&set(s2))
if s1==a1:
    print("it is pangram")
else:
    print("it is not pangram")
