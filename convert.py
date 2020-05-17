import sys
import os.path
from os import path
import time
from datetime import datetime
import timestamp

root_directory = "/home/user/CI5235_K1801286_Sevan/"
evtx_directory = root_directory + "evtx_logs/"
C5235_directory = root_directory + "CI5235_Logs/"

def logo():
    print("   ______                           __                ")
    print("  / ____/___  ____ _   _____  _____/ /_  ____  __  __ ")
    print(" / /   / __ \/ __ \ | / / _ \/ ___/ __/ / __ \/ / / / ")
    print("/ /___/ /_/ / / / / |/ /  __/ /  / /__ / /_/ / /_/ /  ")
    print("\____/\____/_/ /_/|___/\___/_/   \__(_) .___/\__, /   ")
    print("                                     /_/    /____/    \n\n")

def start():
    sys.stdout.write("Checking for CI5235_Logs/ ... ")
    
    if path.exists('CI5235_Logs') == False:
        os.mkdir('CI5235_Logs')
        print("Directory created")
    else:
        print("Directory exists, no changes made")
    print("")
    read()

def read():
    file_count = 0
    directories = os.listdir(evtx_directory)

    print(str(len(directories)) + " directories detected:") # Print number of directories

    for directory in directories: # Scan through directories in evtx_logs
        new_dir = evtx_directory + directory # Adds path name to selected directory in evtx (/logs/persisteynce)
        print(" - " + directory + " has " + str(len(os.listdir(new_dir))) + " files")  # Print directory and number of files inside
        
        file_count = file_count + len(os.listdir(new_dir))
    print("\n", file_count, " total files detected")
    
    check_xml() # Call function to find and delete xml files

    xml_conversion = input("Start evtx > xml conversion? (evtx_dump.py)? (y|n): ")

    if xml_conversion == "y" or xml_conversion == "yes": 
        file_count = 0 # reset count
        
        # Start writing to log file
        clock = timestamp.get_time()
        f = open(C5235_directory + "Convert_Log_" + clock, "w+") # Open File
        
        f.write("Log Date and Time: " + clock + "\r\n")

        print("File conversions commencing:")

        time_start = time.time()

        loading = "[                                    ]" # 20 long
        loading_array = list(loading)
        loading_counter = 2
        x = 0
        for files in directories:
            
            f.write("\r\nConverting files in " + files + " directory:\r\n\r\n")
            print("> " + files) 
            for sub_files in os.listdir(evtx_directory + files):
                f.write(" - Converting '" + sub_files + "' to .xml format...")
                print(" - Converting '" + sub_files + "' to .xml format...")
                xmlfile = evtx_directory + files + "/'" + sub_files[:-5] + ".xml'"

                os.system("python " + root_directory + "evtx_dump.py " + evtx_directory + files + "/'" + sub_files + "' > " + xmlfile) # Conversion command

                file_count = file_count + 1
                f.write("  [+] Conversion done!\r\n")
                print("   [+] Conversion done!")
                if x % 5 == 0:
                    loading_array[loading_counter] = "▇"
                    loading = ''.join(loading_array)
                    loading_counter = loading_counter + 1
                print("\n",loading,"\n")
                x = x + 1
            
        time_end = time.time()
        conversion_time = time_end - time_start

    else:
        print("\n[!] No conversions made.")
        input("\n# Convert.py stopped, press enter to return to main menu #\n")
        os.system("python hello.py")
        sys.exit()

    print("\n# Summary of conversions #\n")
    print("Files converted: ", file_count)
    print("Directories: ", str(len(directories)))
    conv_print = str("Conversion time: %.2f" % conversion_time) + " seconds"
    print(conv_print)
    print("Log files saved to: CI5235_Logs/Convert_Log_" + clock)

    f.write("\r\n# Summary of conversions #\r\n")
    f.write("Files converted: "+ str(file_count))
    f.write("\r\nDirectories: "+ str(len(directories)))
    f.write("\r\n" + conv_print)
    f.close()

    input("\n# Convert.py finished, press enter to return to main menu #")
    os.system("python hello.py")
    sys.exit()

def check_xml():

    checkxml = False
    
    for directories in os.listdir(evtx_directory):
        for file in os.listdir(evtx_directory + directories):
            if file.endswith(".xml"):
                checkxml = True
                break
    
    if checkxml == True:
        delete_xml = input("\n[!] Logs exist, delete to commence? (y/n) :\n")
        if delete_xml  == "y" or delete_xml == "yes":
            del_files()
        else:
            print("[!] No where to convert files to")
            input("\n# Convert.py stopped, press enter to return to main menu #\n")
            os.system("python hello.py")
            sys.exit()

def del_files():
    for directory in os.listdir(evtx_directory):
        for file in os.listdir(evtx_directory + directory):
            if file.endswith(".xml"):
                os.remove(evtx_directory + directory + "/" + file)
        print("[-] " + directory + " xml files removed")

    print("\n[!] All .xml files removed\n")
    

logo()
start()
