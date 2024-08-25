Here are brief descriptions for each task:

1. #*Temperature Conversion*
Implemented a program to convert temperature between Celsius, Fahrenheit, and Kelvin scales, allowing users to input a value and select the conversion type.
def convert_temperature():
    print("Temperature Conversion Program")
    print("-------------------------------")

    # Get user input
    temp_value = float(input("Enter a temperature value: "))
    original_unit = input("Enter the original unit (C/F/K): ").upper()

    # Convert temperature
    if original_unit == "C":
        fahrenheit = (temp_value * 9/5) + 32
        kelvin = temp_value + 273.15
        print(f"{temp_value}°C is equal to:")
        print(f"{fahrenheit}°F")
        print(f"{kelvin} K")
    elif original_unit == "F":
        celsius = (temp_value - 32) * 5/9
        kelvin = (temp_value - 32) * 5/9 + 273.15
        print(f"{temp_value}°F is equal to:")
        print(f"{celsius}°C")
        print(f"{kelvin} K")
    elif original_unit == "K":
        celsius = temp_value - 273.15
        fahrenheit = (temp_value - 273.15) * 9/5 + 32
        print(f"{temp_value} K is equal to:")
        print(f"{celsius}°C")
        print(f"{fahrenheit}°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

convert_temperature()


2. *Guessing Game*
Developed a game where the user has to guess a randomly generated number within a specified range. The program provides hints and tracks the number of attempts until the correct answer is guessed.
import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    guessing_game()


3. *Simple Contact Management System*
Designed a basic contact management system to store and manage contact information, including name, phone number, and email. The system allows users to add, delete, update, and search contacts.

contact={}
def display_contact():
    print("Name\t\tcontact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice=int(input("1.Add new contact:\n 2. Search contact:\n 3.Display Contact:\n 4.Edit Contact:\n 5.Delete Contact:\n 6.Exit:\n Enter your choice:"))
    if choice ==1:
        name = input("enter the contact name:")
        number=input("enter the phone number:")
        print("Successfully added..!!")
        contact[name]=number
    elif choice==2:
        name1=input("enter the contact name:")
        if name1 in contact:
            print("Here we go..!!")
            print(name1,"'s cotact number is",contact[name1])
        else:
            print("Name is not found in contact book")
    elif choice==3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("Enter the contact to be edited:")
        if edit_contact in contact:
            phone=input("enter the mobile number")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choice==5:
        del_contact=input("Enter the contact to be deleted:")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact y/n?")
            if confirm =='y' or confirm=='Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break
    

4. *Sudoku Solver*
Created a program to solve Sudoku puzzles using a backtracking algorithm. The solver takes an incomplete Sudoku grid as input and generates a completed solution.
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("_______")
print_board(board)



6. *Web Scraping*
Built a web scraping tool to extract specific data from websites using Python libraries like BeautifulSoup and Requests. The tool can be used to gather information from online sources.

import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.thewhiskyexchange.com"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
t={}
data=[]
c=0
for x in range(1,6):
    k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={}&psize=24&sort=pasc'.format(x)).text
    soup=BeautifulSoup(k,'html.parser')
    productlist = soup.find_all("li",{"class":"product-grid__item"})


    for product in productlist:
        link = product.find("a",{"class":"product-card"}).get('href')
        productlinks.append(baseurl + link)


for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("p",{"class":"product-action__price"}).text.replace('\n',"")
    except:
        price = None

    try:
        about=hun.find("div",{"class":"product-main__description"}).text.replace('\n',"")
    except:
        about=None

    try:
        rating = hun.find("div",{"class":"review-overview"}).text.replace('\n',"")
    except:
        rating=None

    try:
        name=hun.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
    except:
        name=None

    whisky = {"name":name,"price":price,"rating":rating,"about":about}

    data.append(whisky)
    c=c+1
    print("completed",c)

df = pd.DataFrame(data)

print(df)

These descriptions highlight your programming skills and experience in various areas, including:
