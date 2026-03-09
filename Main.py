import datetime
import time
import random
import uuid
import threading

import math_module
import file_module

from utility_package import welcomemessage


# Stopwatch

def stopwatch():

    input("\nPress ENTER to start stopwatch")

    start = time.time()

    running = True
    def run():

        while running:

            elapsed = int(time.time() - start)

            h = elapsed // 3600
            m = (elapsed % 3600) // 60
            s = elapsed % 60

            print(f"\rRunning Time: {h:02}:{m:02}:{s:02}      ", end="")

            time.sleep(1)

    t = threading.Thread(target=run)

    t.start()

    input("\nPress ENTER to stop stopwatch")

    running = False

    t.join()

    print("\nStopwatch stopped\n")


# Countdown

def countdown():

    seconds = int(input("Enter seconds: "))

    while seconds > 0:

        print(f"\rTime remaining:", seconds)

        time.sleep(1)

        seconds -= 1

    print("Time's up!")


# Datetime menu

def datetime_menu():

    while True:

        print("""
Datetime and Time Operations

1. Display current date and time
2. Calculate difference between two dates/times
3. Format date into custome format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
""")

        c = int(input("Enter choice: "))

        if c == 1:

            now = datetime.datetime.now()

            print("Current Date and Time:", now.strftime("%d-%m-%Y %H:%M:%S"))

        elif c == 2:

            d1 = input("Enter first date (DD-MM-YYYY): ")
            d2 = input("Enter second date (DD-MM-YYYY): ")

            date1 = datetime.datetime.strptime(d1, "%d-%m-%Y")
            date2 = datetime.datetime.strptime(d2, "%d-%m-%Y")

            diff = abs((date2 - date1).days)

            print("Difference:", diff, "days")

        elif c == 3:

            now = datetime.datetime.now()

            formatted = now.strftime("%Y-%m-%d %H:%M:%S")

            print("Formatted Date:", formatted)

        elif c == 4:

            stopwatch()

        elif c == 5:

            countdown()

        elif c == 6:

            break

        else:

            print("Invalid choice")


# Math menu

def math_menu():

    while True:

        print("""
Mathematical Operations

1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometry Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
""")

        c = int(input("Enter choice: "))

        if c == 1:

            n = int(input("Enter number: "))

            print("Factorial:", math_module.factorial(n))

        elif c == 2:

            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = int(input("Years: "))

            print("Compound Interest:", math_module.compound_interest(p,r,t))

        elif c == 3:

            a = float(input("Enter angle: "))

            s,c,t = math_module.trig(a)

            print("Sin:",s)
            print("Cos:",c)
            print("Tan:",t)

        elif c == 4:

            print("""
1. Circle
2. Rectangle
3. Triangle
""")

            shape = int(input("Choice: ")) 

            if shape == 1:

                r = float(input("Radius: "))

                print("Area:", math_module.circle_area(r))

            elif shape == 2:

                l = float(input("Length: "))
                w = float(input("Width: "))

                print("Area:", math_module.rectangle_area(l,w))

            elif shape == 3:

                b = float(input("Base: "))
                h = float(input("Height: "))

                print("Area:", math_module.triangle_area(b,h))

        elif c == 5:

            break


# Random menu

def random_menu():

    while True:

        print("""
Random Data Generation

1. Generate a Random Number
2. Generate a Random List
3. Generate a Random Password
4. Generate a Random OTP
5. Back to the Main Menu
""")

        c = int(input("Enter choice: "))

        if c == 1:

            print("Random Number:", random.randint(1,100))

        elif c == 2:

            print("Random List:", [random.randint(1,50) for _ in range(5)])

        elif c == 3:

             length = int(input("Enter password length (minimum 8): "))

             if length < 8:
                print("Password length must be at least 8 characters")
             else:

                chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+=`~{}[]|:;\"'<>,.?/"

                password = ""

                for i in range(length):

                 password += random.choice(chars)

                print("Generated Password:", password)

        elif c == 4:

            print("OTP:", random.randint(100000,999999))

        elif c == 5:

            break


# UUID

def generate_uuid():

    print("Generated UUID:", uuid.uuid4())



# File menu


def file_menu():

    while True:

        print("""
File Operations:

1. Create a new file
2. Write to a file
3. Read a file
4. Append to a file
5. Back to the Main Menu
""")

        c = int(input("Enter choice: "))

        if c == 1:

            file_module.create_file(input("File name: "))

        elif c == 2:

            name = input("File name: ")
            text = input("Text: ")

            file_module.write_file(name,text)

        elif c == 3:

            file_module.read_file(input("File name: "))

        elif c == 4:

            name = input("File name: ")
            text = input("Text: ")

            file_module.append_file(name,text)

        elif c == 5:

            break


# dir() explorer

def explore_module():

    name = input("Enter module name: ")

    try:

        module = __import__(name)

        print(dir(module))

    except:

        print("Module not found")


# MAIN PROGRAM

if __name__ == "__main__":

    welcomemessage()

    while True:

        print("""
Main Menu

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes (dir())
7. Exit
""")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            datetime_menu()

        elif choice == 2:
            math_menu()

        elif choice == 3:
            random_menu()

        elif choice == 4:
            generate_uuid()

        elif choice == 5:
            file_menu()

        elif choice == 6:
            explore_module()

        elif choice == 7:

            print("Thank you for using the Multi-Utility Toolkit!")

            break
