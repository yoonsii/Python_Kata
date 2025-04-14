def parse_ps_output(filename):
    with open(filename) as f:
        lines = f.readlines()

    # Remove header line
    data_lines = lines[1:]
    
    # Data structures
    cpu_by_user = {}
    mem_by_user = {}
    processes = []  # to store each process dict if you want to do advanced queries

    max_cpu_pid = None
    max_cpu_value = 0.0
    max_mem_pid = None
    max_mem_value = 0.0

    for line in data_lines:
        # Split into 11 parts max
        fields = line.split(None, 10)  
        user = fields[0]
        pid = int(fields[1])
        cpu = float(fields[2])
        mem = float(fields[3])
        command = fields[10]

        # Summaries
        cpu_by_user[user] = cpu_by_user.get(user, 0.0) + cpu
        mem_by_user[user] = mem_by_user.get(user, 0.0) + mem

        # Track max CPU
        if cpu > max_cpu_value:
            max_cpu_value = cpu
            max_cpu_pid = pid

        # Track max MEM
        if mem > max_mem_value:
            max_mem_value = mem
            max_mem_pid = pid

        # If you want to do more advanced queries later:
        processes.append({
            "user": user,
            "pid": pid,
            "cpu": cpu,
            "mem": mem,
            "command": command
        })

    # Print or return results
    print("CPU usage by user:", cpu_by_user)
    print("MEM usage by user:", mem_by_user)
    print(f"Highest CPU usage: PID={max_cpu_pid}, %CPU={max_cpu_value}")
    print(f"Highest MEM usage: PID={max_mem_pid}, %MEM={max_mem_value}")

    # Optional: top 5 by memory or CPU
    # sorted_procs = sorted(processes, key=lambda p: p["cpu"], reverse=True)
    # print("Top 5 CPU processes:", sorted_procs[:5])
