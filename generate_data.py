import sys

from fstring2fst.fstring2fst import create_fst, generate
from fstring2fst.fstring2fst import create_fst, generate



def generate_names(n):
    from full_names import VARIABLES, SENTENCES, OUTPUT
    f, ist, ost = create_fst(VARIABLES, SENTENCES, OUTPUT)
    generate(f, n=n)



def generate_numbers(n):
    from phone_numbers import VARIABLES, SENTENCES, OUTPUT
    f, ist, ost = create_fst(VARIABLES, SENTENCES, OUTPUT)
    generate(f, n=n)


def generate_addresses(n):
    from addresses import VARIABLES, SENTENCES, OUTPUT
    f, ist, ost = create_fst(VARIABLES, SENTENCES, OUTPUT)
    generate(f, n=n)


def generate_kennitala(n):
    from kennitala import VARIABLES, SENTENCES, OUTPUT
    f, ist, ost = create_fst(VARIABLES, SENTENCES, OUTPUT)
    generate(f, n=n)


def print_help():
    print("""
        Usage: python generate_data.py <entity:str> <amount:int>
        E.g.: python generate_data.py phone_number phone_numbes.txt
        Generate data from rules. Supported entities: [name, kennitala, phone_number]
        """)



if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print_help()
            exit()
        entity = sys.argv[1]
        n = int(sys.argv[2])
    except Exception:
        print_help()
        exit()

    if entity == "name":
        generate_names(n)
    elif entity == "phone_number":
        generate_numbers(n)
    elif entity == "address":
        generate_addresses(n)
    elif entity == "kennitala":
        generate_kennitala(n)
    else:
        print_help()
