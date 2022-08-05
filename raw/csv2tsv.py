import csv
import sys

fname = sys.argv[1]
with open(fname, "r") as f:
    reader = csv.reader(f)

    writer = csv.writer(sys.stdout, delimiter="\t")
    for l in reader:
        writer.writerow(l)

