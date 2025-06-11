import argparse
import subprocess
import os

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

filename = args.filename

print(filename)

with open(filename) as file:
    for line in file:
        if line != "":
            path = os.path.normpath(line.strip())

            print(repr(line))
            result = subprocess.run(["du", "-sh", path], capture_output=True, text=True)
            print(result) 


def main():
    print("Entrypoint")


if __name__ == "__main__":

    print(__name__)
    main()