##REMOVE ALL DOUBLE HASHTAGS; These are only for compatibilty with windows / mac and other debugging purposes

# this library (picamera) will flag an error on windows or mac but should run without issues on Linux OS
## from picamera import (PiCamera)
from time import sleep
import datetime  # registers the raspberry pi's internal clock (slippage of 103.8 seconds per month, or a little less than 2 minutes without internet connection)

##camera = PiCamera()
timestamp = datetime.datetime.now().strftime(
    "%d/%m/%Y/%H/%M/%S"
)  # variable that saves pics as date in DD/MM/YYYY/HH/MM/SS
picdir = "C:/Users/puran/Desktop/Data log folder astro/Captured Photos/debug (REASSIGN FOR FLIGHT)/{timestamp}.jpg"  # uses timestamp var and gives save location for pic
picdirfolder = "C:/Users/puran/Desktop/Data log folder astro/Captured Photos/debug (REASSIGN FOR FLIGHT)"
logfile = "log.txt"
log_entry = f"{timestamp}: new picture captured from terminator camera B and saved to {picdirfolder}\n"


def updatetime():
    global timestamp
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y/%H/%M/%S")


while True:
    ##camera.capture({picdir})
    with open(logfile, "a") as log_file:
        log_file.write(log_entry)
    log_entry = f"{timestamp}: new picture captured from terminator camera B and saved to {picdirfolder}\n"
    sleep(5)
    updatetime()
