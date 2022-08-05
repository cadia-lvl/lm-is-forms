
values_is = [
    (9000, "níu þúsund"),
    (8000, "átta þúsund"),
    (7000, "sjö þúsund"),
    (6000, "sex þúsund"),
    (5000, "fimm þúsund"),
    (4000, "fjögur þúsund"),
    (3000, "þrjú þúsund"),
    (2000, "tvö þúsund"),
    (1000, "eitt þúsund"),
    (900, "níu hundruð"),
    (800, "átta hundruð"),
    (700, "sjö hundruð"),
    (600, "sex hundruð"),
    (500, "fimm hundruð"),
    (400, "fjögur hundruð"),
    (300, "þrjú hundruð"),
    (200, "tvö hundruð"),
    (100, "hundrað"),
    (90, "níutíu"),
    (80, "áttatíu"),
    (70, "sjötíu"),
    (60, "sextíu"),
    (50, "fimmtíu"),
    (40, "fjörtíu"),
    (30, "þrjátíu"),
    (20, "tuttugu"),
    (19, "nítján"),
    (18, "átján"),
    (17, "sautján"),
    (16, "sextán"),
    (15, "fimmtán"),
    (14, "fjórtán"),
    (13, "þrettán"),
    (12, "tólf"),
    (11, "ellefu"),
    (10, "tíu"),
    (9, "níu"),
    (8, "átta"),
    (7, "sjö"),
    (6, "sex"),
    (5, "fimm"),
    (4, ["fjórir", "fjórar", "fjögur"]),
    (3, ["þrír", "þrjár", "þrjú"]),
    (2, ["tveir", "tvær", "tvö"]),
    (1, ["einn", "ein", "eitt"]),
]

GENDER_TO_INDEX = {
    "kk": 0,
    "kvk": 1,
    "hk": 2,
}


def get_is_number(n, gender="kk", can_zero=True):
    if can_zero and n == 0:
        return "núll"
    for v, r in values_is:
        if n >= v:
            next = get_is_number(n - v, gender=gender, can_zero=False)
            if type(r) == list:
                R = r[GENDER_TO_INDEX[gender]]
            else:
                R = r
            if not next:
                return R
            if "og" in next:
                return R + " " + next
            else:
                return R + " og " + next
    return ""
