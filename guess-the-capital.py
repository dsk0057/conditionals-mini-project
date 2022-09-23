import csv
import random
from colorama import Fore, Back, Style

# read the csv file and return a reader object
with open("countries.csv", "r") as data:
    reader = csv.reader(data)

    # iterate through reader and put the data in dictionary form
    dict_country_capital = {rows[0]: rows[1] for rows in reader}
    print(dict_country_capital)

# convert the dictionary into list for easier manipulation
country_capital_list = list(dict_country_capital.items())
random_entry = random.choice(country_capital_list)

# Print welcome statement using coloroma's Fore, Back and Style properties
print()
print(f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}-------------Welcome to the Capital Quiz Game--------------")
print(Style.RESET_ALL)

# declare variable for ease of use later
total_countries = (len(dict_country_capital))
# counter for number of attempts
attempts = 0
user_choice = ""


# function for a game of quiz if user inputs "y"
def playquiz():
    global attempts
    # while loop to keep on prompting user until 3 attempts are reached
    while attempts < 3:
        answer = input(f"{Fore.RED}What is the capital of {Fore.GREEN}{random_entry[0]}?: \n{Fore.RESET}")
        answer = answer.lower().strip()
        attempts = attempts + 1
        # check user answer and display if correct and terminate
        if answer == random_entry[1].lower():
            print(f"{Fore.GREEN}Yay! Correct Answer!")
            break
        # output the correct answer once 3 incorrect attempts have been made
        if attempts == 3:
            print(f"{Fore.RED}\nGood try, but not quite! The correct answer was {Fore.GREEN}{random_entry[1]}.")
            break
        else:
            print(f"{Fore.RED}Incorrect answer, please try again.")
        # attempts = attempts + 1


# main function that gets triggered initially during runtime
def main():
    global attempts, user_choice
    # while loop to keep on looping until input is n
    while user_choice != "n":
        print(f"\n{Fore.YELLOW}Would you like to play?")
        print("\nEnter y for Yes.")
        print(f"Enter n for No.{Fore.RESET}")
        user_choice = input()
        # input normalization
        user_choice = user_choice.lower().strip()
        # test different conditions based on user input and display accordingly
        if user_choice == "y":
            print(
                f"{Fore.BLACK}{Back.LIGHTYELLOW_EX}You will get a random country from a list of {total_countries} countries.")
            print("You get 3 attempts to guess the capital. \nAre you ready to test your geo-knowledge?")
            print(Style.RESET_ALL)
            playquiz()
            break
        elif user_choice == "n":
            break
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Try again!")

    # end message for user leaving the game
    print(f"\n{Fore.CYAN}Thank you for visiting! Bye for now.")


# call the main function
if __name__ == "__main__":
    main()
