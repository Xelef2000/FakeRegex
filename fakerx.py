import argparse
import random
import string

from scipy import rand

anchors = [r"^", r"\A", r"$", r"\Z", r"\b", r"\B", r"\<" , r"\>"]
escape_sequences = ["\\", r"\Q", r"\E"]
character_classes = [r"\c", r"\s", r"\S", r"\d", r"\D", r"\w", r"\W", r"\x", r"\O"]
posix = ["[:upper:]", "[:lower:]", "[:alpha:]", "[:alnum:]", "[:digit:]", "[:xdigit:]", "[:punct:]", "[:graph:]", "[:print:]", "[:blank:]", "[:space:]"]
pattern_modifiers = ["g", "i", "m", "s", "x", "U", "u"]
special_characters = [r"\n", r"\r", r"\t", r"\v", r"\f", r"\xxx", r"\xhh" ]

def fake_range():
    length = random.randint(1, 23)
    letters = string.ascii_letters
    
    if random.randint(0, 3) == 0:
        return "[" + letters[length] + "-" + letters[length + random.randint(1, 23)] + "]"
    if random.randint(0, 1) == 0:
        return "[" + letters.upper()[length] + "-" + letters.upper()[length + random.randint(1, 23)] + "]"
    
    
    return "["  + str(random.randint(0, length))  + "-" + str(random.randint(length, 40)) + "]"

def fake_grouping():
    length = random.randint(1, 20)
    return "{"  + str(random.randint(0, length))  + "," + str(random.randint(length, 40)) + "}"

def random_string(length):
    """Generate a random string of length with special characters"""
    return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(length)])

def random_symboles():
    length = random.randint(1, 20)
    return random_string(length)

def random_regex():
    """Generate a random regex"""
    regex = ""
    length = random.randint(1, 20)
    num_operations = 10
    for i in range(length):
        if random.randint(0, num_operations) == 0:
            regex += random.choice(anchors)
        elif random.randint(0, num_operations) == 0:
            regex += random.choice(escape_sequences)
        elif random.randint(0, num_operations) == 0:
            regex += random.choice(character_classes)
        elif random.randint(0, num_operations) == 0:
            regex += random.choice(posix)
        elif random.randint(0, num_operations) == 0:
            regex += random.choice(pattern_modifiers)
        elif random.randint(0, num_operations) == 0:
            regex += random.choice(special_characters)
        elif random.randint(0, num_operations) == 0:
            regex += fake_range()
        elif random.randint(0, num_operations) == 0:
            regex += fake_grouping()
        elif random.randint(0, num_operations) == 0:
            regex += random_symboles()
        else:
            regex += random.choice(string.ascii_letters)
    return regex



def generate_fake_rx(length):
    re = "/" + random.choice(anchors)
    while len(re) < length:
        re += random_regex()

    re += "/" + "".join(random.choices(pattern_modifiers, k=random.randint(1, len(pattern_modifiers))))
    return re


def print_list(ls):
    """Print a list"""
    for i in ls:
        print(i)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fake RX")
    parser.add_argument("-l", "--length", help="Lenght of string", required=True)
    parser.add_argument('-v', '--valid', action='store_true', help='Produce valid Regex')
    parser.parse_args()
    if parser.parse_args().valid :
        print("Not yet implemented")
        exit(1)

    print(generate_fake_rx(int(parser.parse_args().length)))

    # print_list(anchors)
    # print_list(escape_sequences)
    # print_list(character_classes)
    # print_list(posix)
    # print_list(pattern_modifiers)
    # print_list(special_characters)
    # print(fake_range())
    # print(fake_grouping())


  