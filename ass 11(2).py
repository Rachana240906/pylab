import pandas as pd

n = int(input("Enter the number of strings: "))
elements = [input(f"Enter string {i+1} (or leave blank for None): ") or None for i in range(n)]

s = pd.Series(elements)

upper_case = s.str.upper()
lower_case = s.str.lower()
string_length = s.str.len()

print("\nOriginal Series:\n", s)
print("\nUppercase:\n", upper_case)
print("\nLowercase:\n", lower_case)
print("\nLength of strings:\n", string_length)
