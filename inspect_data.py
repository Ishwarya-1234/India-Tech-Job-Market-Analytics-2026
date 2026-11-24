import csv
import os

FILES = [
    "data/raw/skills-demand-india.csv",
    "data/raw/tech-salaries-stated-india.csv"
]

for file_path in FILES:

    print("\n" + "=" * 70)
    print("FILE:", file_path)
    print("=" * 70)

    if not os.path.exists(file_path):
        print("File not found!")
        continue

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        print("\nCOLUMNS:")
        print(reader.fieldnames)

        rows = list(reader)

        print("\nTOTAL ROWS:", len(rows))

        print("\nFIRST 3 ROWS:")
        for row in rows[:3]:
            print(row)