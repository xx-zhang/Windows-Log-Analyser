# Windows-Log-Analyser

A set of python scripts to analyse, present and visualise Windows .evtx log files
This was an assignment I completed for university.

To start, run hello.py:

- python hello.py

Below are the different sections you can find in this script.

convert.py - Check and clear any existing xml files before converting .evtx event log files to .xml files for analysis.

analyse.py - Search for specific event IDs in any .xml files found. Please note: you will not be able to run this without any existing .xml files.

visualise.py - Visualise a log file from analyse.py. Please note: you will not be able to run this without any analyse.py logs.

Event ID information - Search for IDs or terms for descriptions of events. Ref: www.ultimatewindowssecurity.com/securitylog/encyclopedia/

View Logs - View any log files created from convert.py, analyse.py and visualise.py without having to come out of the script.

