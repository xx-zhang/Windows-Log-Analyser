import sys
import os.path
from os import path
import readfile
import time
from datetime import datetime
import timestamp

#root_directory = "/home/user/CI5235_K1801286_Sevan/"
evtx_directory = "evtx_logs/"
C5235_directory = "CI5235_Logs/"

event_IDs = [1102,4611,4624,4634,4648,4661,4662,4663,4672,4673,4688,4698,4699,4702,4703,4719,4732,4738,4742,4776,4798,4799,4985,5136,5140,5142,5156,5158]
eventselection = []

def check_requirements(): # Ensure Log Directory and xml files exist
    if path.exists('CI5235_Logs') == False:
        
        print("[!] No log files exist, you must run convert.py first to continue")
        input("\n # Press enter to return #")
        os.system("python3 hello.py")
        sys.exit()
    
    # Check if xml don't exist
    directories = os.listdir(evtx_directory)
    checkxml = False
    for directories in os.listdir(evtx_directory):
        for file in os.listdir(evtx_directory + directories):
            if file.endswith(".xml"):
                checkxml = True # At least 1 xml file exists!
                break # All good :) lets continue
    if checkxml == False: # If no xml files were found
        print("[!] No xml files exist to analyse, you must run convert.py first to continue")
        input("\n # Press enter to return #")
        os.system("python3 hello.py")
        sys.exit()


def get_events():
    print("\nEnter desired event ID(s) line by line")
    print("Enter an empty input to finish:\n")
    done = False
    x = 1
    while True:
        event_input = input("Enter ID number "+str(x)+": ")
        if event_input == "":
            break
        eventselection.append(event_input)
        x = x + 1
    return eventselection

def validate(up_range, low_range): # Validate input with EH
    
    while True:
        print("\n[1] Analyse default eventIDs")
        print("[2] Analyse specified eventIDs (input)")
        print("[3] Quit\n")
        try:
            selection = int(input(""))
            if selection >= low_range and selection <= up_range:
                return selection
            else:
                print("\n[!] Invalid menu item\n")
        except:
            print("\n[!] Invalid integer\n")

def menu(): 

    check_requirements() # Check Log before starting
    logo() # Print Logo

    selection = validate(3,1) # Validate and return input [upper, lower range, menu selection].
    if selection == 3: # Exit option
        os.system("python3 hello.py")
        sys.exit()
    elif selection == 1: # Default eventIDs
        eventselection = event_IDs # Make eventselection the default IDs
        search(eventselection)
    elif selection == 2: # Enter event IDS
        eventselection = get_events() # Call function to ask for specified IDs
        search(eventselection)

def logo():
    print("    ___                __                              ")
    print("   /   |  ____  ____ _/ /_  __________    ____  __  __ ")
    print("  / /| | / __ \/ __ `/ / / / / ___/ _ \  / __ \/ / / / ")
    print(" / ___ |/ / / / /_/ / / /_/ (__  )  __/ / /_/ / /_/ /  ")
    print("/_/  |_/_/ /_/\__,_/_/\__, /____/\___(_) .___/\__, /   ")
    print("                     /____/           /_/    /____/    \n\n")

def search(eventselection):
    file_count = 0 # Count - Files
    match_count = 0 # Count - Matched IDs
    total_ID_count = 0 # Count - ALL IDs

    clock = timestamp.get_time() # Get time stamp from timestamp.py
    f = open(C5235_directory + "Analyse_Log_" + clock, "w+") # Open File
    
    input("\n# Ready, press enter to run script #")
    f.write("Log Date and Time: " + clock + "\r\n")
    f.write("Searching for the following IDs:\r\n")
    # What a weird way to seperate items with comma to log file:
    comma = ""
    for items in eventselection:
        f.write(comma + str(items)) # Display specified events in log file (Later used for visualising)
        comma = ","
    f.write("\r")
    
    directories = os.listdir(evtx_directory) # For loop counter
    for files in directories:
        for sub_files in os.listdir(evtx_directory + files): # Scan through all files
            current_file = "/" + files + "/" + sub_files # Current file location
            if current_file.endswith(".xml"):
                ids_data = readfile.event_search(current_file, f, eventselection) # Call external script to read file
                match_count = match_count + ids_data[0] # Count matched IDs
                file_count = file_count + 1 # Log count
                total_ID_count = total_ID_count + ids_data[1]

    # Summaries below
    f.write("\r\n# Summary of analysis #\r\n")
    f.write("Total log files read: "+ str(file_count))
    f.write("\r\nTotal matched ID's found: " + str(match_count))
    f.write("\r\nTotal ID's found: " + str(total_ID_count))
    # Console
    print("\nTotal log files read: ", file_count)
    print("Matched IDs: ", match_count)
    print("Total IDs: ", total_ID_count)
    print("Log files saved to: CI5235_Logs/Analyse_Log_" + clock)

menu()
input("\n# Analyse.py finished. Press enter to return to main menu #\n")
os.system("python3 hello.py")