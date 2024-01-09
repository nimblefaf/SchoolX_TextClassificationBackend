import csv, os

os.path.curdir

with open('dicts/scidict.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

def find_term(word: str):
    for term in data:
        if word == term[0]:
            return term
    return ""