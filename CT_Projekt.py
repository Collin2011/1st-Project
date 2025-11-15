import os
import sys
import subprocess
import time

var = ""

def menuct():
    global var
    os.system("cls")
    print("_-= C&T Menu =-_\n\n\n")
    print("This is the Menu by Collin & Torben\n\n\n")
    print("1) Shutdown PC\n2) Exit Program\n")

    var = input("What do you want to do?: ")

    while var not in ["1", "2"]:
        menuct()

    if var == "1":
        password()
    if var == "2":
        exit_menu()

def shutdown():
    subprocess.run("shutdown -p")

def exit_menu():
    os.system("cls")
    yesno = input("\nDo you really want to quit? (y)es / (n)o: ")

    while yesno not in ["y", "n"]:
        exit_menu()
    if yesno == "y":
        sys.exit()
    if yesno == "n":
        menuct()

def password():
    os.system("cls")
    
    var = input("Please enter password: ")

    if var == "932011":
        shutdown()
    elif var == "menu":
        menuct()
    else:
        print("INCORRECT PASSWORD! Please try again.")
        time.sleep(5)
        password()

menuct()

