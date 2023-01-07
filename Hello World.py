# Basic program slightly more advanced than the standard "Hello World"
# program that is over used in beginner programming classes as a way
# to get students' feet wet.

from datetime import datetime
from datetime import date
from os import system, name

# See what system is running and use appropriate command to clear the screen
if name == "nt":
    system("cls")
else:
    system("clear")

# Ask the user for their name
user = input("What is your name? ")

# Greet user by name
print("\nHello, " + user + ". It is nice to meet you!")

# Set date and time to variables
today = date.today()
now = datetime.now()
time = now.strftime("%H:%M")

# Display today's date and the current time
print("Today is", today, "and the current time is", time, "\n\n")