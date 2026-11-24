import csv
import os

SKILLS_FILE = "data/raw/skills-demand-india.csv"
SALARY_FILE = "data/raw/tech-salaries-stated-india.csv"


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


# ==============================
# 1. SKILLS DATA AUDIT
# ==============================

print("=" * 65)
print("SKILLS DATA QUALITY AUDIT")
print("=" * 65)

if os.path.exists(SKILLS_FILE):
    skills = read_csv(SKILLS_FILE)

    print("Total records:", len(skills))

    # Check missing values
    missing = {}
    for column in skills[0].keys():
        count = sum(1 for row in skills if not row[column].strip())
        if count > 0:
            missing[column] = count

    print("\nMissing values:", missing if missing else "None")

    # Check duplicate skills
    skill_names = [row["skill"].strip().lower() for row in skills]
    duplicates = len(skill_names) - len(set(skill_names))
    print("Duplicate skill names:", duplicates)

    # Check duplicate ranks
    ranks = [row["rank"] for row in skills]
    duplicate_ranks = len(ranks) - len(set(ranks))
    print("Duplicate ranks:", duplicate_ranks)

    # Check invalid numeric values
    invalid_numbers = 0

    for row in skills:
        try:
            rank = int(row["rank"])
            jobs = int(row["active_jobs"])
            share = float(row["share_of_tech_jobs_pct"])

            if rank <= 0 or jobs < 0 or share < 0:
                invalid_numbers += 1

        except ValueError:
            invalid_numbers += 1

    print("Invalid numeric records:", invalid_numbers)

    # Check snapshot dates
    dates = set(row["as_of"] for row in skills)
    print("Snapshot dates:", dates)

    windows = set(row["window_days"] for row in skills)
    print("Demand windows:", windows)

else:
    print("Skills dataset not found!")


# ==============================
# 2. SALARY DATA AUDIT
# ==============================

print("\n" + "=" * 65)
print("SALARY DATA QUALITY AUDIT")
print("=" * 65)

if os.path.exists(SALARY_FILE):
    salaries = read_csv(SALARY_FILE)

    print("Total records:", len(salaries))

    # Check missing values
    missing = {}
    for column in salaries[0].keys():
        count = sum(1 for row in salaries if not row[column].strip())
        if count > 0:
            missing[column] = count

    print("\nMissing values:", missing if missing else "None")

    # Check duplicate groups
    groups = [(row["group_type"], row["group"]) for row in salaries]
    duplicate_groups = len(groups) - len(set(groups))
    print("Duplicate group combinations:", duplicate_groups)

    # Check invalid salary values
    invalid_salary = 0
    inconsistent_quartiles = 0

    for row in salaries:
        try:
            sample_count = int(row["stated_salaries"])
            q1 = float(row["lower_quartile_lpa"])
            median = float(row["median_lpa"])
            q3 = float(row["upper_quartile_lpa"])

            if sample_count <= 0 or q1 < 0 or median < 0 or q3 < 0:
                invalid_salary += 1

            if not (q1 <= median <= q3):
                inconsistent_quartiles += 1

        except ValueError:
            invalid_salary += 1

    print("Invalid salary records:", invalid_salary)
    print("Inconsistent quartiles:", inconsistent_quartiles)

    # Snapshot dates and windows
    dates = set(row["as_of"] for row in salaries)
    print("Snapshot dates:", dates)

    windows = set(row["window_days"] for row in salaries)
    print("Salary windows:", windows)

else:
    print("Salary dataset not found!")

print("\nAUDIT COMPLETE")