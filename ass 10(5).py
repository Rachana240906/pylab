import numpy as np

n = int(input("Enter number of strings: "))
elements = [input(f"Enter string {i+1}: ") for i in range(n)]
arr = np.array(elements)

center = np.char.center(arr, 15, fillchar='_')
l_justified = np.char.ljust(arr, 15, fillchar='_')
r_justified = np.char.rjust(arr, 15, fillchar='_')

print("Centered:\n", center)
print("Left Justified:\n", l_justified)
print("Right Justified:\n", r_justified)
