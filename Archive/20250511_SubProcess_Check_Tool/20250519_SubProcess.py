import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

filename = args.filename  

def process_lines(line):
    command_components = line.split()
    output = subprocess.run(line, capture_output=True, shell=True, text=True)
    firstline = ""
    print(f"Command: {line.strip()}")
    print(f"Return Code: {output.returncode}")
    if (output.stdout != ""):
        firstline, *_ = output.stdout.split("\n",1)
    else:
        firstline, *_ = output.stderr.split("\n",1)

    print(f"Output: {firstline}\n")


def main():
    with open(filename) as file:
       for line in file:
        #    print(line)
           process_lines(line)



if __name__ == "__main__":
    main()

