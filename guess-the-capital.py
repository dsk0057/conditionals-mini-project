import csv
import random
import crayons

# file = open("countries.csv")
#
# csvreader = csv.reader(file)
#
# rows = []
#
# for row in csvreader:
#     rows.append(row)
#
# country_capital_dict = {x[0]:x[1] for x in rows}
# print(country_capital_dict)

dict_country_capital = {}

with open("countries.csv", mode="r") as data:
    reader = csv.reader(data)
    dict_country_capital = {rows[0]: rows[1] for rows in reader}

country_capital_list = list(dict_country_capital.items())
print(country_capital_list)
random_entry = random.choice(country_capital_list)
print(random_entry)
print(random_entry[0])
print(random_entry[1])

# (len(dict_country_capital)) -------> 247

print("Would you like to play 'Capital-Quiz'?, Yes(y) or No(n)?: ")
attempts = 0
user_choice = ""


def playquiz():
    global attempts
    while attempts < 3:
        answer = input(f"You get 3 tries to get it right. What is the capital of {random_entry[0]}?: \n")
        answer = answer.lower()
        attempts = attempts + 1
        if answer == random_entry[1].lower():
            print("Yay! Correct Answer!")
            break
        if attempts == 3:
            print(f"Good try, but you didn't get it! The correct answer was {random_entry[1]}")
            break
        else:
            print(f"{crayons.red('Incorrect answer')}, please try again.")
        # attempts = attempts + 1


def main():
    global attempts, user_choice
    while user_choice != "n":
        print("\nEnter y for Yes.")
        print("Enter n for No.")

        user_choice = input("Yes or No?")
        user_choice = user_choice.lower().strip()
        if user_choice == "y":
            playquiz()
            break
        elif user_choice == "n":
            # print("Thank you for visiting. Good bye!")
            break
        else:
            print("Invalid input. Try again!")

    print("\nThank you for visiting! Bye for now.")


main()
