import time
from interface import *


# Checks if the file exists by trying to open it.
def fileExists(name):
    try:
        a = open(name, 'rt')  # RT = Read Text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# Creates a file with the name passed in the function parameter.
def createFile(name):
    try:
        a = open(name, 'wt')  # WT = Write Text
        a.close()
    except:
        print('There was an error creating the file.')


# Saves the user registration.
def setUserData(file_name, user):
    try:
        with open(file_name, 'r+') as a:  # R+ = Read and Write
            lines = a.readlines()

            # Reads line by line in the file
            for line in lines:
                saved_user, _, _, _, _, _ = line.strip().split(';')  # Splits the data in the .txt file into two lists.

                # Checks if the user is already registered.
                if user == saved_user:
                    print('This user already exists!')
                    return

            # If the user does not exist, asks for the password for registration.
            password = input('ENTER YOUR PASSWORD: ')
            verify_password = input('ENTER THE PASSWORD AGAIN: ')

            # Loop to check if the user re-entered the password correctly
            while verify_password != password:
                print('The passwords do not match. Try again!')
                verify_password = input('ENTER THE PASSWORD AGAIN: ')

            # Writes in 'userData.txt' the user information with a score count set to 0.
            a.write(f'{user};{password};0;0;0;0\n')  # Writes user data in userData.txt.

    except Exception as e:
        print(f'There was an error writing the data: {e}')
    else:
        time.sleep(0.5)
        print(f'Registration of {user.upper()} added!')
        a.close()
        time.sleep(1)
        clearConsole()


# Checks if the login data matches the registered data.
def verifyLogin(file_name, user):
    # Sets the number of attempts for the user to enter the correct password.
    attempts = 3

    # While attempts are not exhausted, will continue checking the login.
    while attempts > 0:
        try:
            with open(file_name, 'r+') as f:  # R+ = Read and Write
                lines = f.readlines()
                f.seek(0)  # Goes back to the beginning of the file.

                user_found = False

                # Iterates line by line in the file.
                for line in lines:
                    saved_user, saved_password, _, _, _, _ = line.strip().split(
                        ';')  # Splits the data in the .txt file into two lists.

                    # Checks if the entered user exists.
                    if saved_user == user:
                        user_found = True
                        password = input('ENTER YOUR PASSWORD: ')
                        # Checks if the entered password matches the registered password.
                        if saved_password == password:
                            header('LOGIN SUCCESSFUL!')
                            clearConsole()
                            return True
                        # If the password does not match, decreases an attempt.
                        else:
                            print('INVALID PASSWORD, TRY AGAIN!')
                            attempts -= 1
                            break

                # If the user is not found, decreases an attempt.
                if not user_found:
                    print('USER NOT FOUND, TRY AGAIN!')
                    attempts -= 1
                    user = input('ENTER USERNAME: ')

        except FileNotFoundError:
            print("File not found.")
            return
        except Exception as e:
            print(f"Error verifying login: {e}")
            return

    # If the number of attempts is exhausted, the program ends.
    header('MAXIMUM NUMBER OF ATTEMPTS REACHED!')


# Saves the player's score.
def setPoints(file_name, user, points, wins, losses, ties):
    try:
        with open(file_name, 'r+') as f:  # R+ = Read and Write
            lines = f.readlines()
            f.seek(0)

            # Reads line by line and verifies the user.
            for line in lines:
                data = line.strip().split(';')
                password = data[1]
                # If the user matches the logged-in user, updates the player's statistics.
                if data[0] == user:
                    line = f'{user};{password};{points};{wins};{losses};{ties}\n'
                f.write(line)
            f.truncate()

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error updating points: {e}")


# Gets the player's points.
def getPoints(file_name, user, show=False):
    try:
        a = open(file_name, 'rt')  # RT = Read Text
    except:
        print('There was an error reading the file!')
    else:
        # Reads line by line and checks if the user exists.
        for varLine in a:
            data = varLine.split(';')  # Splits the data in the .txt file into a list.
            # Checks if the user (index 0 of the list) matches the one provided.
            data[0] = data[0].replace('\n', '')  # 0 = Name

            if data[0] == user:
                # Removes the newline character from each list index.
                points = data[2].replace('\n', '')  # 2 = Points
                wins = data[3].replace('\n', '')  # 3 = Wins
                losses = data[4].replace('\n', '')  # 4 = Losses
                ties = data[5].replace('\n', '')  # 5 = Ties

                # If the parameter print is True, prints the player's statistics.
                if show == True:
                    line()
                    print(f'WIN: +100', 'LOSS: -75'.rjust(28))
                    header(f'SCORE: {points}\n',
                           f'WINS: {wins}',
                           f'LOSSES: {losses}',
                           f'TIES: {ties}')

                # Returns the values found in the file.
                return int(points), int(wins), int(losses), int(ties)
        # If no matching data is found, returns default values.
        return 0, 0, 0, 0
    finally:
        a.close()


# Gets the ranking of the highest scores from the .txt.
def getRanking(file_name):
    try:
        a = open(file_name, 'rt')  # RT = Read Text
    except:
        print('There was an error reading the file!')
    else:
        data = []

        # Reads line by line in the file.
        for line in a:
            saved_user, _, points, _, _, _ = line.split(';')  # Splits the data in the .txt file into a list.
            data.append((saved_user, points))  # Adds the user and the points to the data list.

        # Prints the function header
        header('RANKING')
        print(f'{'USER'.rjust(1)} {'POINTS'.center(68)}\n')

        # Creates a list sorted by the highest number of points
        ranking = sorted(data, key=lambda x: x[1], reverse=True)

        # Total length desired for each line
        total_length = 40

        # Loop that prints the points ranking in ascending order of users
        for i, (saved_user, points) in enumerate(ranking):
            ranking = sorted(data, key=lambda x: x[1], reverse=True)  # Updates the ranking list
            free_spaces = total_length - len(saved_user) - len(str(i + 1)) - len(points)

            # Prints the users and their scores from highest to lowest
            print(f'{i + 1}. {saved_user.upper()}{' ' * free_spaces}{points}')
        a.close()
