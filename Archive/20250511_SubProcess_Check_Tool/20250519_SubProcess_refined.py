import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

filename = args.filename  

def process_lines(line):
    
    output = subprocess.run(line, capture_output=True, shell=True, text=True)
    firstline = ""
    
    stdout = output.stdout.strip()
    stderr = output.stderr.strip()
    
    print(f"Command: {line.strip()}")
    print(f"Return Code: {output.returncode}")
    if stdout:
        first_line = stdout.splitlines()[0] # Much better way of getting the first line 
    elif stderr:
        first_line = stderr.splitlines()[0] # Much better way of getting the first line  
        # firstline, *_ = output.stderr.split("\n",1)
    else:
        first_line = "<no output>"

    print(f"Output: {firstline}\n")


def main():
    with open(filename) as file:
       for line in file:
            # Improvement: Skip any line that is blank (rather than forking empty)
            cmd = line.strip() 
            if not cmd or cmd.startswith('#'):
                continue
            process_lines(cmd)



if __name__ == "__main__":
    main()

