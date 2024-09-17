import time
import os

# Prints a line ( ========================================== )
def line(length=42):
    print('=' * length)

# Prints a header with the line() and centered text
def header(*text, length=42):
    line(length)
    for item in text:
        print(item.center(length))
    line(length)

# Prints the menu with the options provided as parameters
def menu(*options):
    for i, option in enumerate(options, start=1):
        print(f'[{i}]. {option}')
    line()

# Clears the console after the time passed as argument
def clearConsole(cooldown = 1):
    import os
    import time

    time.sleep(cooldown) # Wait for the time passed as argument
    # If your IDE doesn't support the clear command, the console will be cleaned by printing 50 blank lines
    for i in range(50):
        print()

    # If your IDE supports the clear command, it will be used
    if os.name == 'nt': # If the OS is Windows
        os.system('cls')
    else: # If the OS is Linux or MacOS
        os.system('clear')
