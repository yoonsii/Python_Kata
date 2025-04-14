import shlex  # this is required to handle spaces in quotes
from collections import defaultdict

timestamp_dict = defaultdict(lambda:1)
logLevel_dict = defaultdict(lambda:1)
userID_dict = defaultdict(lambda:1)
endpoint_dict = defaultdict(lambda:1) 
status_dict = defaultdict(lambda:1)
optionalMessage_dict = defaultdict(lambda:1)

response_codes = {'POST', 'GET', 'PUT'}
count = 0

#timestamp_default_dict = defailt


def updateDict(dict, newValue):
    dict[newValue] += 1

def displayDict(dict): 
    for key in dict:
        print(f"{key} - Count: {dict[key]}")



with open("system_events.log") as file:
    for line in file:
        count += 1
        tokens = shlex.split(line)
        updateDict(timestamp_dict, tokens[0])
        updateDict(logLevel_dict, tokens[1])
        updateDict(userID_dict, tokens[2])

        if tokens[3] in response_codes:
            
            updateDict(endpoint_dict, tokens[3] + " " + tokens[4])

            if len(tokens) == 7:
                updateDict(status_dict, tokens[5] + " - " + tokens[6])
                updateDict(optionalMessage_dict, tokens[6])
            elif len(tokens) == 6:
                updateDict(status_dict, tokens[5])
        
        else:
            updateDict(endpoint_dict, tokens[3])

            if len(tokens) == 6:
                updateDict(status_dict, tokens[4] + " - " + tokens[5])
                updateDict(optionalMessage_dict, tokens[5])
            elif len(tokens) == 5:
                updateDict(status_dict, tokens[4])




print(timestamp_dict)
print(logLevel_dict)
print(userID_dict)
print(endpoint_dict)
print(status_dict)
print(optionalMessage_dict)

displayDict(endpoint_dict)

top_three_endpoint = sorted(endpoint_dict, key=endpoint_dict.get, reverse=True)[:3]

print(top_three_endpoint)
print(f"the number of lines is {count}")




