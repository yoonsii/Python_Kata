import shlex


errorcodes = {} 
loglevels = {}
ipaddresses = {}

line_count = 0

file = open('app.log')





for line in file:
    line_count += 1
    #print(line)
    #for token in shlex.split(line):
    #    print(token)
    print(shlex.split(line)[6])
    
    errorcode = shlex.split(line)[6]
    
    if errorcode in errorcodes:
        #print(f'key {errorcode} is found - incrementing')
        errorcodes[errorcode] += 1
    else:
        #print(f'key {errorcode} not found - adding to dictionary')
        errorcodes[errorcode] = 1

    loglevel = shlex.split(line)[2]

    if loglevel in loglevels:
        loglevels[loglevel] += 1
    else:
        loglevels[loglevel] = 1
    
    ipaddress = shlex.split(line)[3]

    if ipaddress in ipaddresses:
        ipaddresses[ipaddress] += 1
    else:
        ipaddresses[ipaddress] = 1




print(errorcodes)
print(f'Linecount: {line_count}')
print(loglevels)
print(ipaddresses)

top_three_ip = sorted(ipaddresses, key=ipaddresses.get, reverse=True)[:3]
print(top_three_ip)