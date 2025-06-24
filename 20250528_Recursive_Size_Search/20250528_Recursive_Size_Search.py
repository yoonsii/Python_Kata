import argparse
import subprocess
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

filename = args.filename

FILE_THRESHOLD = 300

#print(filename)




def main():
    with open(filename) as file:
        for line in file:
            if line.strip() != "" and not line.startswith("#"):
                path = os.path.normpath(line.strip())

                #print(repr(line))
                result = subprocess.run(["du", "-sh", path], capture_output=True, text=True)
                #print(result) 
                print(result.stdout.strip())

                rstdout = result.stdout.split('\t')[0].strip()
                print(rstdout.strip())

                match = re.match(r"(\d+)", rstdout)
                if match:
                    digits = match.group(1)
                    print(digits)  # Output: 123


if __name__ == "__main__":

    #print(__name__)
    main()