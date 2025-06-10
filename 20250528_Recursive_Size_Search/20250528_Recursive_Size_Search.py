import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

filename = args.filename

print(filename)

with open(filename) as file:
    for line in file:
        if line != "":
            print(line)
            result = subprocess.run(["du", "-sh", line.strip()], capture_output=True, text=True)
            print(result) 


def main():
    print("Entrypoint")


if __name__ == "__main__":

    print(__name__)
    main()