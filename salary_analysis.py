import csv

SALARY_FILE = "data/raw/tech-salaries-stated-india.csv"


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


salaries = read_csv(SALARY_FILE)


def print_salary_table(title, records):
    print("\n" + "=" * 95)
    print(title)
    print("=" * 95)

    print(
        f"{'Category':<36}"
        f"{'Sample':>8}"
        f"{'Q1':>10}"
        f"{'Median':>10}"
        f"{'Q3':>10}"
        f"{'Spread':>10}"
    )
    print("-" * 95)

    for row in records:
        q1 = float(row["lower_quartile_lpa"])
        median = float(row["median_lpa"])
        q3 = float(row["upper_quartile_lpa"])
        spread = q3 - q1

        print(
            f"{row['group']:<36}"
            f"{int(row['stated_salaries']):>8}"
            f"{q1:>10.2f}"
            f"{median:>10.2f}"
            f"{q3:>10.2f}"
            f"{spread:>10.2f}"
        )


# ==========================================
# 1. OVERALL SALARY
# ==========================================

overall = [
    row for row in salaries
    if row["group_type"] == "overall"
]

print_salary_table("OVERALL SALARY DISTRIBUTION", overall)


# ==========================================
# 2. SALARY BY EXPERIENCE
# ==========================================

experience = [
    row for row in salaries
    if row["group_type"] == "experience"
]

experience_order = {
    "0–1 years": 1,
    "2–4 years": 2,
    "5–8 years": 3,
    "9+ years": 4
}

experience.sort(
    key=lambda row: experience_order.get(row["group"], 99)
)

print_salary_table("SALARY BY EXPERIENCE", experience)


# ==========================================
# 3. SALARY BY ROLE FAMILY
# ==========================================

roles = [
    row for row in salaries
    if row["group_type"] == "role_family"
]

roles.sort(
    key=lambda row: float(row["median_lpa"]),
    reverse=True
)

print_salary_table("SALARY BY ROLE FAMILY (HIGHEST MEDIAN FIRST)", roles)


# ==========================================
# 4. SALARY BY SKILL
# ==========================================

skills = [
    row for row in salaries
    if row["group_type"] == "skill"
]

skills.sort(
    key=lambda row: float(row["median_lpa"]),
    reverse=True
)

print_salary_table("SALARY BY SKILL (HIGHEST MEDIAN FIRST)", skills)


# ==========================================
# 5. FIND WIDEST SALARY SPREAD
# ==========================================

print("\n" + "=" * 95)
print("WIDEST SALARY SPREADS (Q3 - Q1)")
print("=" * 95)

all_groups = [
    row for row in salaries
    if row["group_type"] in ("experience", "role_family", "skill")
]

all_groups.sort(
    key=lambda row: (
        float(row["upper_quartile_lpa"])
        - float(row["lower_quartile_lpa"])
    ),
    reverse=True
)

for row in all_groups[:5]:
    spread = (
        float(row["upper_quartile_lpa"])
        - float(row["lower_quartile_lpa"])
    )

    print(
        f"{row['group_type']:<15} "
        f"{row['group']:<35} "
        f"Spread: {spread:.2f} LPA"
    )


print("\nSALARY ANALYSIS COMPLETE")