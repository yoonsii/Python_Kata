import argparse


VALID_KEYS = ['username', 'password', 'host', 'port']

def process_line(line, keys_dict):
    splitline = line.replace("\n","").split("=")
    keys_dict[splitline[0]] = splitline[1]
    return keys_dict
    
def find_missing_keys(keys_dict):
    missing = [word for word in VALID_KEYS if word not in keys_dict]
    return missing

def find_missing_values(keys_dict):
    present = [word for word in VALID_KEYS if word in keys_dict]
    return present

def print_missing_values(keys_dict):
    for key in keys_dict:
        print(key, end=" ")



def main():

    conf_pairs = {}

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename

    print(f"Filename: {filename}")

    with open(filename) as file:
        for line in file:
            process_line(line, conf_pairs)

    missing = find_missing_keys(conf_pairs)
    missing_values = find_missing_values(conf_pairs)
    print(f"Missing: {', '.join(missing_values)}")

if __name__ == "__main__":
    main()