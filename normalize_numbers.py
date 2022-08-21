from spell_number import get_is_number
import sys


def read_file(fname):
    if fname == "-":
        f = sys.stdin
    else:
        f = open(fname)
    for l in f:
        yield l


def split_phone_number(n):
    n = n.replace(" ", "")
    PATTERNS = [
        "{} {} {} {} {} {} {}",
        "{} {}{} {}{}{}{}",
        "{} {}{} {}{} {}{}",
        "{} {} {} {}{} {} {}",
        "{}{} {}{} {} {} {}",
        "{}{} {}{} {}{}{}",
        "{} {}{} {} {} {} {}",
        "{} {} {} {}{} {} {}",
        "{} {} {} {} {} {}{}",
    ]
    for pattern in PATTERNS:
        split = pattern.format(*list(n))
        if not any([len(s) > 1 and s[0] == "0" for s in split.split(" ")]):
            yield split


def split_kennitala(n):
    n = n.replace("-", "")
    PATTERNS = [
        "{} {} {} {} {} {} {} {} {} {}",
        "{}{} {}{} {}{} {}{} {}{}",
        "{}{} {}{} {}{} {}{} {} {}",
        "{}{} {}{} {}{} {} {} {}{}",
        "{}{} {}{} {}{} {} {} {} {}",
        "{}{} {}{} {} {} {} {} {} {}",
        "{}{} {}{} {} {} {} {} {}{}",
        "{}{} {}{} {} {} {}{} {} {}",
        "{}{} {}{} {} {} {}{} {}{}",
        "{} {} {}{} {} {} {}{} {}{}",
        "{}{} {} {} {}{} {}{} {}{}",
    ]
    for pattern in PATTERNS:
        split = pattern.format(*list(n))
        if not any([len(s) > 1 and s[0] == "0" for s in split.split(" ")]):
            yield split


def phone_nubmer(number):
    number = number.strip()
    return " ".join([get_is_number(int(n), gender="kk") for n in number.split(" ")])


def kennitala(number):
    number = number.strip()
    return " ".join([get_is_number(int(n), gender="kk") for n in number.split(" ")])


def print_help():
    print("""
        Usage: python normalize_numbers.py <entity:str> <in_file:str>
        E.g.: python normalize_numbers.py phone_number phone_numbes.txt
        Normalize numerical data. Supported entities: [kennitala, phone_number]
        """)


if __name__ == "__main__":
    try:
        entity = sys.argv[1]
        fname = sys.argv[2]
    except Exception:
        print_help()
        exit()

    if entity == "kennitala":
        for n in read_file(fname):
            for s in split_kennitala(n):
                print(kennitala(s))
    elif entity == "phone_number":
        for n in read_file(fname):
            for s in split_phone_number(n):
                print(phone_nubmer(s))
    else:
        print_help()
