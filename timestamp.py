import time
from datetime import datetime

def get_time():
    # Time Stamp
    d = datetime.now()
    timestamp = d.strftime("%d_%b_%Y_%H:%M:%S")
    return timestamp