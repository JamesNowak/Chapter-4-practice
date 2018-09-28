# TODO 4.5 Sentinel Value
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Have the user enter test scores until a sentinel value of -1 is
# entered.
# Display the total, the count and the average (total / count)
total = 0
score = 0
count = 0
print("Enter a test score ")
print("Or enter -1 to end.")
while score != -1:
    count = count + 1
    score = int(input("Enter a test score: "))
    total = total + score

print("The average perecentage is", (total / count))
