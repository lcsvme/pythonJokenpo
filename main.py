from interface import *  # Imports functions from the interface module.
from arquivo import *  # Imports functions from the arquivo module.
import random
import time

file_name = 'userData'  # Defines the name of the file to be created.

# Checks if a file already exists in the system.
if not fileExists(file_name):
    createFile(file_name)  # If not, creates a file.


# Gets the option (Login, Register, Exit) from the user.
def getUserData():
    # Prints the choice menu for the user.
    header('LOGIN')
    menu('Login',
         'Register',
         'Exit')

    user_option = input('ENTER THE NUMBER OF YOUR OPTION: ')
    options = {'1': 'Login', '2': 'Register', '3': 'Exit'}  # Dictionary with options.

    # Checks if the user entered a valid option.
    if user_option in options:
        return options[user_option]
    # If not, prints an error message.
    else:
        print('INVALID OPTION! PLEASE TRY AGAIN!')
        return getUserData()  # Calls the function again for the user to enter a valid option.


# Gets the choice (Rock, Paper, Scissors) from the user.
def getUserChoice():
    # Prints the choice menu for the user.
    header('ROCK PAPER SCISSORS')
    menu('Rock', 'Paper', 'Scissors', 'View Score', 'View Ranking', 'Exit')

    user_choice = input('ENTER THE NUMBER OF YOUR CHOICE: ')
    choices = {'1': 'Rock', '2': 'Paper', '3': 'Scissors', '4': 'View Score', '5': 'View Ranking',
               '6': 'Exit'}  # Dictionary with options.

    # Checks if the user entered a valid choice.
    if user_choice in choices:
        return choices[user_choice]
    # If not, prints an error message.
    else:
        print('INVALID CHOICE! PLEASE TRY AGAIN!')
        return getUserChoice()  # Calls the function again for the user to enter a valid choice.


# Gets the computer's random choice.
def getComputerChoice():
    choices = ['Rock', 'Paper', 'Scissors']  # List of available choices for the computer.
    return random.choice(choices)  # Returns a random choice for the computer.


# Determines the winner of the current round.
def getWinner(user_choice, computer_choice):
    # Shows the choices made by the user and the computer.
    print(f'YOUR CHOICE: {user_choice}')
    print('THE COMPUTER CHOSE... ', end='')
    time.sleep(1)
    print(computer_choice)

    # Checks if the game is a tie.
    if user_choice == computer_choice:
        return 'TIE!'
    # Checks if the user won the round.
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Paper' and computer_choice == 'Rock') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return 'YOU WON!'
    # If none of the above, the user lost the round.
    else:
        return 'YOU LOST!'


# Manages the game flow, handling user login, running game rounds, and updating scores.
def playGame():
    # While the user is not logged in, they cannot play!
    while True:
        user_option = getUserData()  # Stores the return value of getUserData() in user_option.

        # If the user chooses to exit, the program will terminate.
        if user_option == 'Exit':
            header('EXITING!')
            return
        # If the user chooses to log in, it will verify the credentials.
        elif user_option == 'Login':
            user = input('ENTER USERNAME: ').strip().lower()
            if verifyLogin(file_name, user):
                break
        # If the user chooses to register, it will request the registration details.
        elif user_option == 'Register':
            user = input('ENTER USERNAME: ').strip().lower()
            setUserData(file_name, user)

            # If login is successful, the game will start.
    while True:
        user_choice = getUserChoice()  # Stores the return value of getUserChoice() in user_choice.

        # Gets the user's points, wins, losses, and ties from the .txt file, without printing the results.
        points, wins, losses, ties = getPoints(file_name, user, show=False)

        # If the user chooses to exit, the program will terminate.
        if user_choice == 'Exit':
            header('EXITING!')
            return
        # If the player chooses to view the score, it will show the data and continue the game.
        elif user_choice == 'View Score':
            clearConsole()
            getPoints(file_name, user, True)
            sair = input('PRESS ANYTHING TO CONTINUE... ')
            time.sleep(1.5)
            continue
        # If the player chooses to view the ranking, it will show the ranking and continue the game.
        elif user_choice == 'View Ranking':
            clearConsole()
            getRanking(file_name)
            line()
            sair = input('PRESS ANYTHING TO CONTINUE... ')
            time.sleep(1.5)
            continue

        computer_choice = getComputerChoice()  # Stores the return value of getComputerChoice() in computer_choice.
        result = getWinner(user_choice, computer_choice)  # Stores the return value of getWinner() in result.
        time.sleep(1)
        header(result)
        time.sleep(1)

        # Updates the score count
        if result == 'YOU WON!':
            clearConsole(0.75)
            wins += 1  # Updates the win count
            points += 100  # Updates the points

        elif result == 'YOU LOST!':
            clearConsole(0.75)
            losses += 1  # Updates the loss count
            # Updates the points, not allowing the user to have negative points.
            if points >= 75:
                points -= 75
            if points == 50:
                points -= 50
            if points == 25:
                points -= 25

        elif result == 'TIE!':
            clearConsole(0.75)
            ties += 1  # Updates the tie count

        setPoints(file_name, user, points, wins, losses, ties)


# Starts the game
if __name__ == "__main__":
    playGame()
