# -*- coding: utf-8 -*-
import os
import sys
from readfile import event_IDs
import glob
import time

def logo(option): # Print Logos

    if option == 1:
        print(" _       ___           __                       __                   _    ___                       ")
        print("| |     / (_)___  ____/ /___ _      _______    / /   ____  ____ _   | |  / (_)__ _      _____  _____")
        print("| | /| / / / __ \/ __  / __ \ | /| / / ___/   / /   / __ \/ __ `/   | | / / / _ \ | /| / / _ \/ ___/")
        print("| |/ |/ / / / / / /_/ / /_/ / |/ |/ (__  )   / /___/ /_/ / /_/ /    | |/ / /  __/ |/ |/ /  __/ /    ")
        print("|__/|__/_/_/ /_/\__,_/\____/|__/|__/____/   /_____/\____/\__, /     |___/_/\___/|__/|__/\___/_/     ")
        print("                                                        /____/                                      ")

    if option == 2:
        print(" _    ___                 __                    ")
        print("| |  / (_)__ _      __   / /   ____  ____ ______")
        print("| | / / / _ \ | /| / /  / /   / __ \/ __ `/ ___/")
        print("| |/ / /  __/ |/ |/ /  / /___/ /_/ / /_/ (__  ) ")
        print("|___/_/\___/|__/|__/  /_____/\____/\__, /____/  ")
        print("                                  /____/        ")

    if option == 3:
        print("    ______                 __     ____        __        __                   ")
        print("   / ____/   _____  ____  / /_   / __ \____ _/ /_____ _/ /_  ____ _________  ")
        print("  / __/ | | / / _ \/ __ \/ __/  / / / / __ `/ __/ __ `/ __ \/ __ `/ ___/ _ \ ")
        print(" / /___ | |/ /  __/ / / / /_   / /_/ / /_/ / /_/ /_/ / /_/ / /_/ (__  )  __/ ")
        print("/_____/ |___/\___/_/ /_/\__/  /_____/\__,_/\__/\__,_/_.___/\__,_/____/\___/  ")

    if option == 4:
        print("\n\n   _____                                                     _       __ ")
        print("  / ___/___  ___     __  ______  __  __   ____ _____ _____ _(_)___  / / ")
        print("  \__ \/ _ \/ _ \   / / / / __ \/ / / /  / __ `/ __ `/ __ `/ / __ \/ /  ")
        print(" ___/ /  __/  __/  / /_/ / /_/ / /_/ /  / /_/ / /_/ / /_/ / / / / /_/   ")
        print("/____/\___/\___/   \__, /\____/\__,_/   \__,_/\__, /\__,_/_/_/ /_(_)    ")
        print("                  /____/                     /____/                     \n\n\n")

def list_logs(listdir): # List Logs in /CI5235_Logs
    print("\n Select file to view: \n")

    while True: # Persistance until valid input
        for x in range(len(listdir)): # Read through files in directory
            files = listdir[x]
            print("["+str(x+1)+"] "+files[12:]) # List files for menu

        try:
            selection = int(input("\n")) # Check if input is int
            if selection >= 1 and selection <= len(listdir): # Check if input is in range
                print("Just before returning:",selection)
                return selection
            else:
                print("\n[!] Invalid menu item\n")
        except:
            print("\n[!] Invalid integer\n")

def view_logs(): # View Log Function
    logo(2) 
    print("Select type of Log to view\n")
    print("[1] Convert_Log files")
    print("[2] Analyse_Log files")
    print("[3] Visdata_Log files")
    print("[4] Exit\n")

    try:
        selection = int(input("")) # Check 
    except:
        print("\n[!] Invalid integer\n")
        view_logs()
    
    if selection >= 1 and selection <= 4:
        if selection == 1:
            listdir = glob.glob("CI5235_Logs/Convert*") # List all Convert logs
        elif selection == 2:
            listdir = glob.glob("CI5235_Logs/Analyse*") # List all Analyse logs
        elif selection ==  3:
            listdir = glob.glob("CI5235_Logs/Visdata*") # List all Visualise logs
        elif selection == 4:
            run()
            sys.exit()
        
    else:
        print("\n[!] Invalid menu item\n")
        view_logs()

    file_selection = list_logs(listdir) # List files for Log type and get selection
    print("file selection",file_selection)
    f = open(listdir[file_selection-1])
    filelines = f.readlines()

    for line in filelines:
        print(line)
    
    input("\n# Showing Specified Log File, press enter to continue # ")
    view_logs()
    
def log_info():
    logo(3)
    
    print("\nWelcome to the Windows Security Log Events page!")
    print("You may enter any query such as event IDs or description words:")
    print("Input '/default' to view the 28 event IDs used in analyse.py")
    print("Input '/quit' to return to the main menu\n")

    f = open("datasheet") # Open Event info datasheet
    found = False 
    default = False

    select = input("") # Search query for datasheet. No EH as its a general search term

    if select == "/quit": # Stop search session
        run()
        sys.exit()

    elif select == "/default": # Use default event IDs
        default = True

    line = f.readline()
    while line: # Read through each line
        if default == True: # Only execute if default event IDs selected
            for event in event_IDs:
                if str(event) == line[:4]: # Comparison of
                    print(line)
            found = True
            
        if default == False:
            if select in line:
                print("\n[+] Found!")
                print(line)
                found = True
        line = f.readline()
    
    if found == False:
        print("\n[!] Query not found in database")
        log_info()

    elif found == True:
        input("# Press enter to continue #")
        log_info()

def print_menu():
    logo(1)
    print("\n\nPlease select item: ")
    print("\n[1] convert.py")
    print("[2] analyse.py")
    print("[3] visualise.py")
    print("[4] Event ID information")
    print("[5] View Logs")
    print("[6] Quit\n")

def val_input():
    menu_selection = -1 # Initiate as invalid option
    isValid = False 
    while not isValid: # Peristance menu, only allowing int in range
        print_menu()
        try:
            menu_selection = int(input(""))
            if (menu_selection >= 0) and (menu_selection <= 6):
                isValid = True
                return menu_selection
            else:
                print("\n[!] Invalid menu item\n")
        except:
            print("\n[!] Invalid integer\n")

def run():
    menu_selection = val_input()

    if menu_selection == 1: # Convert
        os.system("python3 convert.py")
        input()
    elif menu_selection == 2: # Analyse
        os.system("python3 analyse.py")
        input()
    elif menu_selection == 3: # Visualise
        os.system("python3 visualise.py")
    elif menu_selection == 4: # Event ID information
        log_info()
    elif menu_selection == 5: # View Logs
        view_logs()
    else: # Quit
        logo(4)
        sys.exit()
    #done

run()
sys.exit()