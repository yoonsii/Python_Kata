import argparse


VALID_KEYS = ['username', 'password', 'host', 'port']

def process_line(line, keys_dict):
    parts = line.strip().split("=", 1)
    if len(parts) == 2:
        key, value = parts
        keys_dict[key] = value
    return keys_dict
    
def find_missing_keys(keys_dict):
    missing = [word for word in VALID_KEYS if word not in keys_dict]
    return missing

# Optional Not in Spec but made for learning purposes
def print_keys_with_blank_values(keys_dict):
    for key in VALID_KEYS:
        if keys_dict.get(key, None) is not None and keys_dict[key].strip() == "":
            print(f"The key: {key} is missing a value.")



def main():

    conf_pairs = {}

    # Commmented out for ease of testing - hardcoded filename only for testing
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

    print_keys_with_blank_values(conf_pairs)

    print(f"Missing: {', '.join(missing_keys)}")

if __name__ == "__main__":
    main()