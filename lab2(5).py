students = []

for i in range(10):
    name = input("Enter student name: ")
    if len(name) > 15:
        name = name[:15]
    students.append(name)

for name in students:
    print(name[::-1])
