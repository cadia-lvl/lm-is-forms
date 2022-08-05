
address = [
    "{street}",
]
neighborhood = [
    "{postal_code} {city}",
    "{city}",
]
full_address = [
    "{address}",
    "{address}, {neighborhood}",
]

VARIABLES = {
    "street_nf": "raw/street_nf.lst",
    "street_tgf": "raw/street_tgf.lst",
    "number": "raw/house_number.lst",
    "postal_code": "raw/postnumer.lst",
    "city": "raw/city.lst",
}
SENTENCES = {
    "street": ["{street_nf}", "{street_tgf}"],
    "address": address,
    "neighborhood": neighborhood,
    "full_address": full_address,
}
OUTPUT = "full_address"