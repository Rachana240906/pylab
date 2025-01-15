num = int(input("Enter a number: "))
rnum = 0
while num != 0:
    rnum = rnum * 10 + num % 10
    num //= 10
print("Reversed number:", rnum)
