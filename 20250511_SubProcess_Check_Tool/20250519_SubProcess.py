import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

print(args.filename)
filename = args.filename

#with open(filename) as file:
#    for line in file:
#        print(line)

with open(filename) as file:
    line = file.readline()

    command_components = line.split()


print(line)
print(command_components)

output = subprocess.run(line, capture_output=True, shell=True, text=True)
print(output)

print(f"Return Code: {output.returncode}")
print(f"stdout: {output.stdout}")
print(f"stderr: {output.stderr}")


