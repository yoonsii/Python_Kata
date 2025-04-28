from datetime import datetime
from datetime import timedelta
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("filename")
args = parser.parse_args()
filename = args.filename


now = datetime.now()
now_test = "2025-04-26 09:25:44"

# Setting now to an artificial time for purposes of this exercise
now = datetime.strptime(now_test, '%Y-%m-%d %H:%M:%S')
now = now.replace(microsecond=0)

recent_now = now - timedelta(minutes=5)

MIN_ERROR = 10

# DEBUG
print(f"The time now is: {now}")
print(f"The time 5 mins ago was: {recent_now}")

print(args.filename)

def scan_logs(filename):
    with open(filename) as file:

        count = 0
        recent_count = 0 # To track errors within the last 5 mins

        for line in file:
            procline = line.split("]")
            date = procline[0][1:]
            line_datetime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            if "ERROR".lower() in line.lower():
                count += 1

            if line_datetime > recent_now and line_datetime < now: # The 'and' wouldn't be required as in real situation we wouldn't have log entries 'in the future'
                #print("within 5 mins")
                if "ERROR".lower() in line.lower():
                    recent_count += 1

            # DEBUG
            # print("hmm:" ,line_datetime)
            # print("now:" , recent_now)
        
        print(f"The error count is: {count}")
    
    if recent_count > MIN_ERROR:
        f = open(f"error_{filename}", "x")
        f.write(f"There have been {recent_count} errors in {filename} in the last 5 mins")
    


if __name__ == "__main__":

    scan_logs(filename)
    