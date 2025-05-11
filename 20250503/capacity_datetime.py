from datetime import datetime, timedelta
from collections import defaultdict

number_of_days = 30

FILENAME = "files_listing.txt"

CURRENT_TIME = datetime.now().replace(microsecond=0)
CUTOFF_DURATION = timedelta(days=number_of_days, microseconds=0)
CUTOFF_DATE = CURRENT_TIME - CUTOFF_DURATION

print(f"cutoff date is:  {CUTOFF_DATE}")

size_dict = defaultdict(int)




def process_line(line):
    parts = line.split(" ", 3)
    return parts


with open(FILENAME) as file:
    for line in file:  
        # print(line)
        l_date, l_time, l_size, *_ = process_line(line)
        line_date = datetime.strptime(l_date + " " + l_time, "%Y-%m-%d %H:%M") # %d/%m/%y %H:%M
        if line_date > CUTOFF_DATE:
            # print("within 30 days")
            # print(line)
            size_dict[l_date] += int(l_size)

print(size_dict)

number_of_keys = len(size_dict)

total_size = 0

for key in size_dict:
    print(size_dict[key])
    total_size += size_dict[key]


average_size = total_size / number_of_keys

print(average_size / (1024 * 1024), "MB")




        


# with open(FILENAME) as file:
#     line = file.readline() 
#     #print(line)
#     l_date, l_time, l_size, *_ = process_line(line)
#     # print(l_date + " " + l_time)
    
#     line_date = datetime.strptime(l_date + " " + l_time, "%Y-%m-%d %H:%M") # %d/%m/%y %H:%M

#     print("Line date:",line_date)
#     print("cutoff date:", CUTOFF_DATE)

#     if line_date > CUTOFF_DATE:
#         print("within 30 days")




# usualdict = {}

# tempdict["hii"] += 10
# print(tempdict["hii"])

# usualdict["A"] += 10