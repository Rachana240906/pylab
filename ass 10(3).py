import numpy as np

def odd_magic_square(n):
    magic = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic[i, j] = num
        ni, nj = (i - 1) % n, (j + 1) % n
        if magic[ni, nj]:
            i = (i + 1) % n
        else:
            i, j = ni, nj
    return magic

def doubly_even_magic_square(n):
    magic = np.arange(1, n * n + 1).reshape(n, n)
    mask = np.ones((n, n), dtype=bool)
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                mask[i, j] = False
    magic[~mask] = (n * n + 1) - magic[~mask]
    return magic

def singly_even_magic_square(n):
    half = n // 2
    sub_square = odd_magic_square(half)
    magic = np.zeros((n, n), dtype=int)
    add = [0, 2 * half * half, 3 * half * half, half * half]
    for i in range(half):
        for j in range(half):
            magic[i, j] = sub_square[i, j] + add[0]
            magic[i, j + half] = sub_square[i, j] + add[1]
            magic[i + half, j] = sub_square[i, j] + add[2]
            magic[i + half, j + half] = sub_square[i, j] + add[3]
    k = half // 2
    for i in range(half):
        for j in range(k):
            if j == 0 and i == k:
                continue
            magic[i, j], magic[i + half, j] = magic[i + half, j], magic[i, j]
        for j in range(n - k + 1, n):
            magic[i, j], magic[i + half, j] = magic[i + half, j], magic[i, j]
    return magic

def generate_magic_square(n):
    if n % 2 == 1:
        return odd_magic_square(n)
    elif n % 4 == 0:
        return doubly_even_magic_square(n)
    else:
        return singly_even_magic_square(n)

for size in [4, 5, 6, 7, 8]:
    print(f"\nMagic Square of size {size}:")
    print(generate_magic_square(size))
