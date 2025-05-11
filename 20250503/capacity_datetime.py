from datetime import datetime, timedelta
from collections import defaultdict

NUMBER_OF_DAYS = 30

FILENAME = "files_listing.txt"

CURRENT_TIME = datetime.now().replace(microsecond=0)
CUTOFF_DURATION = timedelta(days=NUMBER_OF_DAYS, microseconds=0)
CUTOFF_DATE = CURRENT_TIME - CUTOFF_DURATION


print(f"Scanning files - Cutoff date is:  {CUTOFF_DATE}")
size_dict = defaultdict(int)




def process_line(line):
    parts = line.split(" ", 3)
    return parts

def str_to_datetime(l_date, l_time):
    return datetime.strptime(l_date + " " + l_time, "%Y-%m-%d %H:%M") # %d/%m/%y %H:%M 

def calculate_dict_average(size_dict):
    number_of_keys = len(size_dict)
    total_size = 0

    for key in size_dict:
        print(size_dict[key])
        total_size += size_dict[key]


    average_size = total_size / number_of_keys
    return average_size

def convert_to_MB(amount): 
    return amount / (1024 * 1024)




def main():
    # process_line()
    with open(FILENAME) as file:
        for line in file:  
            # print(line)
            l_date, l_time, l_size, *_ = process_line(line)
            line_date = str_to_datetime(l_date, l_time)
            if line_date > CUTOFF_DATE:
                # print("within 30 days")
                # print(line)
                size_dict[l_date] += int(l_size)

    #print(size_dict)


    average_size = calculate_dict_average(size_dict)

    print(f"Average usage over {NUMBER_OF_DAYS} days: {convert_to_MB(average_size)} MB")
        


if __name__ == "__main__":
    main()












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