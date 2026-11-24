import csv

SKILLS_FILE = "data/raw/skills-demand-india.csv"
SALARY_FILE = "data/raw/tech-salaries-stated-india.csv"


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


# ==========================================
# 1. SKILL DEMAND ANALYSIS
# ==========================================

skills = read_csv(SKILLS_FILE)

print("=" * 65)
print("INDIA TECH JOB MARKET - SKILL DEMAND")
print("=" * 65)

print("\nTOP 15 MOST DEMANDED SKILLS\n")

for row in skills[:15]:
    print(
        f"{row['rank']:>3}. "
        f"{row['skill']:<25} "
        f"{int(row['active_jobs']):>8,} jobs  "
        f"{float(row['share_of_tech_jobs_pct']):>6.1f}%"
    )

# Top skills by percentage
top_10 = skills[:10]

print("\nTOP 10 SKILLS - MARKET SHARE")
for row in top_10:
    print(
        f"{row['skill']:<25} "
        f"{float(row['share_of_tech_jobs_pct']):>6.1f}%"
    )


# ==========================================
# 2. SALARY ANALYSIS
# ==========================================

salaries = read_csv(SALARY_FILE)

print("\n" + "=" * 65)
print("INDIA TECH JOB MARKET - SALARY ANALYSIS")
print("=" * 65)

# Overall salary benchmark
overall = [
    row for row in salaries
    if row["group_type"] == "overall"
]

print("\nOVERALL SALARY BENCHMARK\n")

for row in overall:
    print("Group:", row["group"])
    print("Salary sample size:", row["stated_salaries"])
    print("Lower quartile:", row["lower_quartile_lpa"], "LPA")
    print("Median salary:", row["median_lpa"], "LPA")
    print("Upper quartile:", row["upper_quartile_lpa"], "LPA")


# Salary by group type
group_types = sorted(set(row["group_type"] for row in salaries))

print("\nAVAILABLE SALARY CATEGORIES")
for group_type in group_types:
    records = [
        row for row in salaries
        if row["group_type"] == group_type
    ]
    print(f"\n{group_type.upper()} ({len(records)} records)")

    for row in records:
        print(
            f"{row['group']:<30} "
            f"Sample: {row['stated_salaries']:>5}  "
            f"Q1: {row['lower_quartile_lpa']:>6}  "
            f"Median: {row['median_lpa']:>6}  "
            f"Q3: {row['upper_quartile_lpa']:>6}"
        )

print("\n" + "=" * 65)
print("EDA COMPLETE")
print("=" * 65)