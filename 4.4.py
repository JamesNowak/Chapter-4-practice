# TODO 4.4 a running total
# Have the user enter 5 numbers, provide a total at the end
# You can assume integers

MAX = 5
total = 0.0

print("This program calcualtes the some of ")
print(max, "numbers you will enter.")

for counter in range(MAX):
    number = int(input("Enter a number: "))
    total = total + number
print("The total is", total)
