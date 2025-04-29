import argparse

def process_line(line):

    conf_pairs = {}
    # print(line)
    splitline = line.replace("\n","").split("=")
    if not splitline == "":
        print(splitline)
    
    conf_pairs[splitline[0]] = splitline[1]

    print(conf_pairs)
    
    


def main():



    filename = "db1.conf"

    # parser = argparse.ArgumentParser()
    # parser.add_argument("test", help="This is here as a test - look this is cool")
    # args = parser.parse_args()
    # print(parser.test)


    with open(filename) as file:
        for line in file:
            process_line(line)


if __name__ == "__main__":
    main()