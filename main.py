import sqlite3
import colorama
from art import text2art
import os
import time
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:  
        os.system('clear')
Title = text2art("Prota 17222 Scouting App", font="Shadow-small")
def create_database():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_database()
def insert_answer(name, question, answer):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO answers (name, question, answer)
        VALUES (?, ?, ?)
    ''', (name, question, answer))
    conn.commit()
    conn.close()

def retrieve_answers_by_name(name):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        SELECT * FROM answers WHERE name = ?
    ''', (name,))
    rows = c.fetchall()
    conn.close()
    return rows

def ask_questions():
    clear()
    name  = input("what is the team number: ")
    questions = [
        "How many points can be scored in autonomous",
        "Where does the robot park in autonomous",
        "How many points can be scored in Tele-Op",
        "How many points can be scored in Endgame"
    ]

    for question in questions:
        answer = input(question + ": ")
        insert_answer(name, question, answer)
    print(colorama.Fore.GREEN + "results saved")
    time.sleep(5)
def display_answers():
    clear()
    name = input("Enter the team number to retrieve answers: ")
    answers = retrieve_answers_by_name(name)
    if answers:
        for row in answers:
            print( colorama.Fore.BLUE + f"Name: {row[1]},", colorama.Fore.MAGENTA + f"Question: {row[2]},", colorama.Fore.LIGHTGREEN_EX + f"Answer: {row[3]}")
    else:
        print(colorama.Fore.RED + "No answers found for this team number.")
    time.sleep(10)
def delete_data():
    clear()
    name = input("Enter the team number that you want to remove: ")
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        DELETE FROM answers WHERE name = ?
    ''', (name,))
    conn.commit()
    conn.close()
    print(colorama.Fore.GREEN + f"ALL data for team {name} has been deleted...")
    time.sleep(3)
def main():
    colorama.init()  
    create_database()
    while True:
        clear()
        print(colorama.Fore.MAGENTA + Title + colorama.Style.RESET_ALL)
        print("1. Enter Information")
        print("2. Retrieve Information")
        print("3. Delete Information")
        print("4. Exit")
        option = input("Enter An Option: ")
        
        if option == '1':
            ask_questions()
        elif option == '2':
            display_answers()
        elif option == '3':
            delete_data()
        elif option == '4':
            break
        else:
            print(colorama.Fore.RED + "Invalid choice. Please choose again." + colorama.Style.RESET_ALL)


if __name__ == "__main__":
    main()