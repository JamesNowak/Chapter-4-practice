# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data

number = int(input("Select a number 1-10: "))
if number <= 0:
    while number <= 0:
        print("Invalid number")
        number = int(input("Select a number 1-10: "))
else:
        while number > 10:
            print("Invalid number")
            number = int(input("Select a number 1-10: "))
        print("Thank you for the valid number!")
