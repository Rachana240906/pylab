T = int(input())
for _ in range(T):
    N = input()
    n = int(N)
    count = 0
    for digit in N:
        if digit != '0' and n % int(digit) == 0:
            count += 1
    print(count)
