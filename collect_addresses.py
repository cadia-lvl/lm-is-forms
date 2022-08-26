import sys
import csv
import string
import re
from spell_number import get_is_number


SPECIAL_CHARS = "áéíúýóðþæö"
SPECIAL_CHARS_UPPER = SPECIAL_CHARS.upper()
ALLOWED_CHARACTERS = string.ascii_uppercase + string.ascii_lowercase + SPECIAL_CHARS + SPECIAL_CHARS_UPPER
ABBR = {
    "v.": "við",
    "nr.": "númer",
    "no.": "númer",
    "bíl.": "bílskúr",
    "bílast.": "bílastæði",
    "flugv.": "flugvöllur",
    "sumarb.l.": "sumarbústaðarlóð",
    "sbl.": "sumarbústaðarlóð",
    "sumarh.lóð": "sumarhúsalóð",
    "samkomuh.": "samkomuhús",
    "útiv.sv.": "útivistarsvæði",
    "íb.lóð": "íbúðarlóð",
    "mhl.": "mhl",
    "hreðavatnsl.": "Hreðavatnsl",
    "bakki.": "bakki",
    "v.hl.": "við hlið",
    "aðk.": "aðkoma",
}

IGNORE = [t.lower() for t in [
    "Munaðarnesl.BSRB",
    "R.A.F.sumarhús",
    "Reykjahlíðarflugv.",
    "bensínst.",
    "Desjam.",
    "Norðl.vegur",
    "félagsh.",
    "Grafarholt.",
    "shl.",
    "Suðurlandsv.",
    "Snorrast.",
    "Lyngbr.",
    "íþr.völlur",
    "Norlb.",
    "Elliðav.",
    "Reynisvl.",
    "Landsp.",
    "Blikast.",
    "Stangarholtsl.",
    "Snæfoksst.",
    "landgræðslusv.",
    "Hraunsholtsv.Hraunsholt",
    "Félagsrækt.",
    "vatnst.",
    "norður.",
    "Gaulv.b.hr.",
    "Norðurbr.",
    "Kollsst.sel",
    "landsp.",
    "ehf.",
    "Nesk.vegar",
    "Lands.Ísl.tækj.",
    "Sumarb.lóð",
    "Skógr.v.",
    "Sumarh.",
    "körfubv.",
    "Bústaðav.",
    "Austurv.",
    "BL.",
    "Kjal.",
    "Kollaf.",
    "a.hl.",
    "O.R.",
    "Stangarholtsl.",
    "Staðarfellsl.",
    "Vatnsendabl.",
    "Miðg.",
    "vikurg.",
    "sv.og",
    "landsp.",
    "Snorrast.tún",
]]


def read_registry(fpath):
    with open(fpath, "r", newline="") as f:
        reader = csv.DictReader(f)
        for l in reader:
            yield l


def clean_address(address):
    return address[:address.rfind("(")].strip()


def validate(address):
    return all(s == " " or s in ALLOWED_CHARACTERS for s in address)


def is_int(token):
    try:
        t = int(token)
        return True
    except ValueError:
        return False


def tokenize(address):
    address = address.replace("  ", " ")
    tokens = [t for t in address.split(" ") if t != ""]
    for token in tokens:
        if any(i in token for i in string.digits):
            match_after = re.match(r"([a-záéíúýóðþæö]+)([0-9]+)", token, re.I)
            match_before = re.match(r"([0-9]+)([a-záéíúýóðþæö]+)", token, re.I)
            match_before = re.match(r"([0-9]+)([a-záéíúýóðþæö]+)", token, re.I)
            if match_before:
                for m in match_before.groups():
                    yield m
            elif match_after:
                for m in match_after.groups():
                    yield m
            else:
                yield token
        else:
            yield token


def normalize_address(address):
    address = address.replace(" v/", " við ")
    address = address.replace(" no.", " númer ")
    address = address.replace(" nr.", " númer ")
    address = address.replace("Nr.", "Númer ")
    address = address.replace("&", " og ")
    address = address.replace("/", " ")
    address = address.replace(",", " ")
    address = address.replace("(", " ")
    address = address.replace(")", " ")
    address = address.replace("*", " ")
    address = address.replace("!", " ")
    address = address.replace("?", " ")
    address = address.replace("1.", "fyrsta ")
    address = address.replace("2.", "önnur ")
    address = address.replace("3.", "þriðja ")
    address = address.replace("4.", "fjórða ")
    address = address.replace("5.", "fimmta ")
    address = address.replace("17.", "sautjánda ")
    tokens = list(tokenize(address))
    new_tokens = []
    for i, token in enumerate(tokens):
        if is_int(token):
            new_tokens.append(get_is_number(int(token), gender="hk"))
        elif token == "-":
            try:
                if is_int(tokens[i-1]) and is_int(tokens[i+1]):
                    new_tokens.append("til")
                else:
                    return ""
            except IndexError:
                return ""
        elif token == "nr.":
            new_tokens.append("númer")
        elif token.lower() in ABBR.keys():
            new_tokens.append(ABBR[token.lower()])
        elif token == ".":
            pass
        elif token.lower().strip() in IGNORE:
            new_tokens.append(token.replace(".", ""))
        else:
            new_tokens.append(token)
    address = " ".join(new_tokens)
    return address


def print_help():
    print("""
        Usage: python collect_addressres.py <registry:str> <outfile:str>
        E.g.: python generate_data.py raw/Stadfangaskra.csv data/addresses.txt
        Collect and normalize addresses from Stadfangaskra.
        """)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print_help()
            exit()
        fname = sys.argv[1]
        ofile = sys.argv[2]
    except Exception:
        print_help()
        exit()
    
    if ofile == "-":
        ofile = sys.stdout
    else:
        ofile = open(ofile, "w")
    
    for address in read_registry(fname):
        a = address["VEF_BIRTING"]
        a = clean_address(a)
        oa = a
        a = a.replace("-", " - ")
        a = normalize_address(a)
        if validate(a):
            if a:
                print(a, file=ofile)
        else:
            print("Unknown character in address: {} ({})".format(oa, a), file=sys.stderr)
