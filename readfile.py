import sys
import os.path
import re
import timestamp
root_directory = "/home/user/CI5235_K1801286_Sevan/"
evtx_directory = root_directory + "evtx_logs/"

event_IDs = [1102,4611,4624,4634,4648,4661,4662,4663,4672,4673,4688,4698,4699,4702,4703,4719,4732,4738,4742,4776,4798,4799,4985,5136,5140,5142,5156,5158]

def get_systime(line, f):
    while line:
        
        if 'TimeCreated' in line:
            sanitise = re.search('Time="(.*)">', line)
            eventtime = sanitise.group(1)
            break
        line = f.readline()
    return eventtime

def event_search(location, fwrite, eventselection):
    matched_count = 0
    total_count = 0
    
    f = open(evtx_directory + location)
    
    line = f.readline()
    while line: # Goes through every line of file
        if 'EventID Qualifiers' in line: # Finds lines with eventID

            total_count = total_count + 1 # Keeps count of total matched IDs

            sanitise = re.search('">(.*)</', line) # Cut numbers out
            eventid = sanitise.group(1)

            eventtime = get_systime(line, f) #Find sys time of this occasion

            for counter in eventselection: # Check against each event_ID 
                if str(counter) == str(eventid):
                    check_match = True
                    break
                else:
                    check_match = False

            print("\nDate and time of event: " + eventtime)
            fwrite.write("\rDate and time of event: " + eventtime)
            print("File Location: ", location)
            fwrite.write("\r\nFile Location: " + location)


            if check_match == True: # When eventID match the array
                print("[+] Matched ID: ", eventid)
                fwrite.write("\r\n[+] Matched ID: "+ eventid+"\r\n")
                matched_count = matched_count + 1
            else:
                print("[-] Unmatched ID: ", eventid)
                fwrite.write("\r\n[-] Unmatched ID: "+ eventid+"\r\n")

        line = f.readline() # Next line of file
    f.close()
    
    return (matched_count, total_count)


