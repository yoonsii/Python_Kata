import json
from collections import defaultdict
import shlex #actually don't need this
from collections import Counter

count = 0
filename = "events.jsonl"
user_id_dict = defaultdict(int) # Providing a lambda that returns 1 to set the default dict key to 1 (instead of 0)
actions_counter = Counter()



def process(line):
    processed_line = json.loads(line)
    print(processed_line["timestamp"])
    user_id_dict[processed_line["user_id"]] += 1
    actions_counter[processed_line["action"]] += 1

    
    


with open(filename) as file:
    for line in file:
        count += 1
        process(line)
    

print(f"File processed: {filename}")
print(f"Linecount: {count}")
print(user_id_dict)
print(actions_counter)
print(f"The number of pairs in actions counter: {len(actions_counter)}")


