import glob
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import graph
import timestamp
import os
import sys
import os.path
from os import path

root_directory = "/home/user/CI5235_K1801286_Sevan/"
C5235_directory = root_directory + "CI5235_Logs/"
event_IDs = [1102,4611,4624,4634,4648,4661,4662,4663,4672,4673,4688,4698,4699,4702,4703,4719,4732,4738,4742,4776,4798,4799,4985,5136,5140,5142,5156,5158]
idlist = {}
count_array = []
item_array = []

def check_log_file(): # Ensure logs directory exists. Can't continue without logs!
    if path.exists('CI5235_Logs') == False:
        
        print("[!] No log files exist, you must run convert.py first to continue")
        input("\n # Press enter to return #")
        os.system("python hello.py")
        sys.exit()

def logo(): # Display Logos accordingly
    print(" _    ___                  ___                         ")
    print("| |  / (_)______  ______ _/ (_)_______    ____  __  __ ")
    print("| | / / / ___/ / / / __ `/ / / ___/ _ \  / __ \/ / / / ")
    print("| |/ / (__  ) /_/ / /_/ / / (__  )  __/ / /_/ / /_/ /  ")
    print("|___/_/____/\__,_/\__,_/_/_/____/\___(_) .___/\__, /   ")
    print("                                      /_/    /____/    \n\n")

def print_menu(listdir): # List out menu options
    print("# Select Log file to visualise, or 0 to quit #\n")
    for x in range(0,len(listdir)): # Read through files in directory
        files = listdir[x]
        print("["+str(x+1)+"] "+files[12:]) # List files for menu
    
def validate(): # Validate input
    listdir = glob.glob("CI5235_Logs/Analyse*") # Create array with only "Analyse"
    menu_selection = -1 # Initiate as invalid option
    while True: # Peristance menu, only allowing int in range
        print_menu(listdir)
        try:
            menu_selection = int(input("\n"))
            if (menu_selection >= 1) and (menu_selection < len(listdir)+1): # Ensure selection in range
                selection = listdir[menu_selection-1]
                return selection
            elif menu_selection == 0:
                return "exit"
            else:
                print("\n[!] Invalid menu item\n")
        except:
            print("\n[!] Invalid integer\n")

def count_ID(selection):

    print(selection, "selected!")
    print("Discovering Matched ID's...\n")
    
    # Sanitise list of eventIDs from log file
    f = open(root_directory + selection, "r") # Open 

    print(root_directory + selection)

    filelines = f.readlines() # Create array with all lines of the file
    interesting_line = filelines[2] # Gets 3rd line of file with events
    eventselection = interesting_line.split(",") # List of event selections
    eventselection[-1] = eventselection[-1].strip() # Take off weird \n from last item in list
    
    for item in eventselection: idlist[int(item)] = {'Count':0} # Initialise empty array

    for line in filelines:# Counting function
        if '[+]' in line:
            eventid = int(line[16:]) # Sanitised number for comparing
            idlist[eventid]['Count'] = idlist[eventid]['Count'] + 1 # Incrament key value if event id matched

def get_graph_data(clock): # Get data from log file to display in graph

    vis_file = open(C5235_directory + "Visdata_Log_" + clock) # Reopen log file

    line = vis_file.readline()

    while line: # Loops through all IDs in Log file
        if 'Count' in line:
            sanitise = line[7:]
            count_array.append(int(sanitise)) # Append ID to counting array
        line = vis_file.readline()
    return count_array

def run():
    logo()
    selection = validate() # Select log file to analyse
    if selection == "exit": # Exit option 
        os.system("python hello.py")
        sys.exit()
    
    count_ID(selection) # Count IDs
    
    clock = timestamp.get_time() # Get time
    fw = open(C5235_directory + "Visdata_Log_" + clock, "w+") # Create Log file
    fw.write("Matched Event ID statistics:\r\n\r\n")

    for ids, info in idlist.items(): # Print out each item and values in dictionary
        print("Event ID:", ids)
        fw.write("Event ID: " + str(ids) +"\n")
        item_array.append(ids) # Append all IDs to array for graph

        for key in info: # Print out nested dictionary
            print(key + ':', info[key],"\n")
            fw.write(str(key) + ': ' + str(info[key]) + "\n\n")
    fw.close()
    input("\n# Log file saved. Press enter to visualise data #")
    count_array = get_graph_data(clock)
    graph.draw_graph(item_array, count_array) # Call script to draw graph

check_log_file()
run()
input("# Done, enter to cont. #")
os.system("python hello.py")