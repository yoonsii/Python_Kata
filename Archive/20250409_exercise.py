# Calculate or extract the following

# 1. Which process or (PID) is using the highest %MEM  x 
# 2. Which process or is using the highest %CPU x
# 3. A summary of total %CPU usage by user (e.g. sum of all CPU usage from processes owned by the same USER)
# 4. A summary of total %MEM usage by user (similarily, sum all MEM usage)
# 5. (Optional) The top 5 processes by memory usage or CPU usage

from collections import Counter
from collections import defaultdict

#unique_users = set()
cpu_by_user = defaultdict(float)
mem_by_user = defaultdict(float)

cpu_by_pid = Counter()
mem_by_pid = Counter()

max_cpu_amount = 0.0
max_cpu_pid = ""

max_mem_amount = 0.0
max_mem_pid = ""

def extract_max_cpu(line):
    global max_cpu_amount,max_cpu_pid
    if float(line[2]) > max_cpu_amount:
        max_cpu_amount = float(line[2])
        max_cpu_pid = line[1]

def extract_max_mem(line):
    global max_mem_amount,max_mem_pid
    if float(line[3]) > max_mem_amount:
        max_mem_amount = float(line[3])
        max_mem_pid = line[1]
    

with open("/home/yoonsi/kata-python/Archive/ps_output.txt") as file:
    for line in file:
        split_line = line.split(None, 10)
        if (split_line[0] == 'USER'):
            continue
        user = split_line[0]
        pid = split_line[1]
        cpu_usage = split_line[2]
        mem_usage = split_line[3]

        cpu_by_pid[pid] += float(cpu_usage)
        #unique_users.add(user)  
        
        cpu_by_user[user] += float(cpu_usage)

        extract_max_cpu(split_line)
        extract_max_mem(split_line)


        
print(cpu_by_user)
print(mem_by_user)
print(f"Process using the most cpu is {max_cpu_pid} and it is using {max_cpu_amount}%")

print(f"Process using the most mem is {max_mem_pid} and it is using {max_mem_amount}%")

print(cpu_by_pid)
top_five = (sorted(cpu_by_pid, key=cpu_by_pid.get, reverse=True)[:5])

print("Here are the top five pids and their cpu usage:")
for key in top_five:
    print(f'pid: {key} usage: {cpu_by_pid[key]}')