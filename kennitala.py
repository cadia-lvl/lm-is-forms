VARIABLES = {
    "day": [f"{i:0>2}" for i in range(1,32)],
    "company_day": [f"{i:0>2}" for i in range(41, 72)],
    "month": [f"{i:0>2}" for i in range(1,13)],
    "year": [f"{i:0>2}" for i in range(0,100)],
    "digit": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    "century": [8, 9, 0],
}

SENTENCES = {
    "kennitala": [
        "{day}{month}{year}-{digit}{digit}{digit}{century}",  # Person
        "{company_day}{month}{year}-{digit}{digit}{digit}{century}",  # Company
    ],
}

OUTPUT = "kennitala"
