feet = float(input("Enter the length in feet: "))

print("Choose a conversion option:")
print("1. Inches")
print("2. Yards")
print("3. Miles")
print("4. Millimeters")
print("5. Centimeters")
print("6. Meters")
print("7. Kilometers")

choice = int(input("Enter the number corresponding to your choice: "))

if choice == 1:
    result = feet * 12
    print(f"{feet} feet is equal to {result} inches.")
elif choice == 2:
    result = feet / 3
    print(f"{feet} feet is equal to {result} yards.")
elif choice == 3:
    result = feet / 5280
    print(f"{feet} feet is equal to {result} miles.")
elif choice == 4:
    result = feet * 304.8
    print(f"{feet} feet is equal to {result} millimeters.")
elif choice == 5:
    result = feet * 30.48
    print(f"{feet} feet is equal to {result} centimeters.")
elif choice == 6:
    result = feet * 0.3048
    print(f"{feet} feet is equal to {result} meters.")
elif choice == 7:
    result = feet / 3280.84
    print(f"{feet} feet is equal to {result} kilometers.")
else:
    print("Invalid choice. Please enter a number between 1 and 7.")
