# import sys

# print("Hello World!")
# print("This is an error message!", file=sys.stderr)

import sys, random

print("Welcome to Form 4 Hope 2022 Class Students.")

first = (
    "Kelvin",
    "Aila",
    "Onkoba",
    "Michael",
    "Harvey",
    "Samuel",
    "George",
    "Nimrod",
    "Maxwell",
    "Kelly",
)

last = (
    "Njuguna",
    "Aila",
    "Misiani",
    "Kennedy",
    "Mburu",
    "kariuki",
    "Kinundu",
    "Paul",
    "Mike",
)

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n\n")
    # print("{} {}".format(firstName, lastName), file=sys.stderr)
    print(f" {firstName}, {lastName}")
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break
input("\nPress Enter to exit")
