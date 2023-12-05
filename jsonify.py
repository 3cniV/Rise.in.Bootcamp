import datetime
import requests
import sys
 
# Usage function
def print_usage(args):
    print('Usage:', sys.argv[0] , '<url>')
    print('Example:', sys.argv[0], 'http://www.google.com')
    sys.exit(1)
 
# Check arguments
if len(sys.argv) != 2:
    print_usage(sys.argv)
else:
    url = sys.argv[1]
 
# Open log file for appending
log_path = 'D:\\Logs\\webcheck.log'
try:
    log_file = open(log_path,'a')
except IOError as e:
    print("Error: ", e)
    sys.exit(1)
 
# Get the current time
currDate = datetime.datetime.now()
currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
 
# Initalise message
message = currDate + "\t" + url 
 
# Try to connect
try:
    r = requests.get(url, timeout=6)
    r.raise_for_status()
    respTime = str(round(r.elapsed.total_seconds(), 2))
    message = message + "\t\t" + respTime
    print(message)
    log_file.write(message + "\n")
except requests.exceptions.RequestException as e:
    message = message + "\t\t" + "RequestException: " + str(e)
    print(message)
    log_file.write(message + "\n")
 
# Close the file
log_file.close()