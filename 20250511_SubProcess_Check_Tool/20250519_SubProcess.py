import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

def main():
    print(args.filename)
    filename = args.filename

    #with open(filename) as file:
    #    for line in file:
    #        print(line)

    with open(filename) as file:
        line = file.readline()

        command_components = line.split()


    # print(line)
    print(command_components)

    # Note - 

    output = subprocess.run(line, capture_output=True, shell=True, text=True)
    print(output)

    firstline = ""


    print(firstline)


    print(f"Command: {line}")
    print(f"Return Code: {output.returncode}")
    if (output.stdout != ""):
        firstline, *_ = output.stdout.split("\n",1)
    else:
        firstline, *_ = output.stderr.split("\n",1)

    print(f"Output: {firstline}")


if __name__ == "__main__":
    main()

