import argparse


VALID_KEYS = ['username', 'password', 'host', 'port']

def process_line(line, keys_dict):
    if not (line == "" or "\n"):
        splitline = line.replace("\n","").split("=")
        keys_dict[splitline[0]] = splitline[1]
    return keys_dict
    
def find_missing_keys(keys_dict):
    missing = [word for word in VALID_KEYS if word not in keys_dict]
    return missing

def find_existing_keys(keys_dict):
    present = [word for word in VALID_KEYS if word in keys_dict]
    return present

# Optional Not in Spec but made for learning purposes
def print_missing_values(keys_dict):
    # print('test')
    for key in keys_dict:
        if keys_dict[key] == "":
            print(f"The key: {key} is missing a value.")



def main():

    conf_pairs = {}

    # parser = argparse.ArgumentParser()
    # parser.add_argument("filename")
    # args = parser.parse_args()
    # filename = args.filename
    filename = "db1.conf"

    print(f"File: {filename}")


    with open(filename) as file:
        for line in file:
            process_line(line, conf_pairs)


    missing_keys = find_missing_keys(conf_pairs)

    # print_missing_values(conf_pairs)

    print(f"Missing: {', '.join(missing_keys)}")

if __name__ == "__main__":
    main()