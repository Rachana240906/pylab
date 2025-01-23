equivalence_classes = {0: [], 1: [], 2: [], 3: [], 4: []}

for num in range(1, 10001):
    remainder = num % 5
    equivalence_classes[remainder].append(num)

all_numbers = set(range(1, 10001))
union_of_classes = set(equivalence_classes[0] + equivalence_classes[1] + equivalence_classes[2] + equivalence_classes[3] + equivalence_classes[4])

if all_numbers == union_of_classes:
    print("The equivalence classes are valid. They cover the entire set from 1 to 10000.")
else:
    print("The equivalence classes are invalid. They do not cover the entire set.")
