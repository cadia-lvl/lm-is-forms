VARIABLES = {
    "name_kvk": "raw/names_kvk.txt",
    "name_kk": "raw/names_kk.txt",
    "surname_kvk": "raw/surnames_kvk.txt",
    "surname_kk": "raw/surnames_kk.txt",
}
SENTENCES = {
    "name": [
        "{name_kvk} {surname_kvk}",
        "{name_kvk} {middle_name_kvk} {surname_kvk}",
        "{name_kk} {surname_kk}",
        "{name_kk} {middle_name_kk} {surname_kk}",
    ],
    "middle_name_kk": [
        "{name_kk}",
        "{name_kk} {name_kk}",
    ],
    "middle_name_kvk": [
        "{name_kvk}",
        "{name_kvk} {name_kvk}",
    ]
}
OUTPUT = "name"