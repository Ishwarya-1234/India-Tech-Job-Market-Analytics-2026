import csv

SKILLS_FILE = "data/raw/skills-demand-india.csv"
SALARY_FILE = "data/raw/tech-salaries-stated-india.csv"


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


skills_data = read_csv(SKILLS_FILE)
salary_data = read_csv(SALARY_FILE)

# Create skill demand lookup
demand_lookup = {
    row["skill"].strip().lower(): row
    for row in skills_data
}

# Keep only salary records for individual skills
skill_salaries = [
    row for row in salary_data
    if row["group_type"] == "skill"
]

# Match skills across the two datasets
matched_skills = []

for salary in skill_salaries:
    skill_name = salary["group"].strip()
    demand = demand_lookup.get(skill_name.lower())

    if demand:
        matched_skills.append({
            "skill": skill_name,
            "jobs": int(demand["active_jobs"]),
            "demand_pct": float(demand["share_of_tech_jobs_pct"]),
            "sample": int(salary["stated_salaries"]),
            "median_salary": float(salary["median_lpa"]),
            "q1": float(salary["lower_quartile_lpa"]),
            "q3": float(salary["upper_quartile_lpa"])
        })

# Calculate thresholds using matched skills
demand_threshold = sorted(
    row["jobs"] for row in matched_skills
)[len(matched_skills) // 2]

salary_threshold = sorted(
    row["median_salary"] for row in matched_skills
)[len(matched_skills) // 2]


# --------------------------------------------------
# 1. COMBINED SKILL DATA
# --------------------------------------------------

print("=" * 100)
print("INDIA TECH MARKET - SKILL DEMAND VS SALARY")
print("=" * 100)

print(f"Matched skills: {len(matched_skills)}")
print(f"Demand threshold: {demand_threshold:,} jobs")
print(f"Salary threshold: {salary_threshold:.2f} LPA")

print("\nALL MATCHED SKILLS")
print("-" * 100)

print(
    f"{'Skill':<32}"
    f"{'Jobs':>12}"
    f"{'Demand %':>12}"
    f"{'Median LPA':>14}"
    f"{'Sample':>10}"
)
print("-" * 100)

matched_skills.sort(
    key=lambda row: row["jobs"],
    reverse=True
)

for row in matched_skills:
    print(
        f"{row['skill']:<32}"
        f"{row['jobs']:>12,}"
        f"{row['demand_pct']:>11.1f}%"
        f"{row['median_salary']:>14.2f}"
        f"{row['sample']:>10}"
    )


# --------------------------------------------------
# 2. HIGH DEMAND + HIGH SALARY
# --------------------------------------------------

high_demand_high_salary = [
    row for row in matched_skills
    if row["jobs"] >= demand_threshold
    and row["median_salary"] >= salary_threshold
]

high_demand_high_salary.sort(
    key=lambda row: row["median_salary"],
    reverse=True
)

print("\n" + "=" * 100)
print("HIGH DEMAND + HIGH SALARY SKILLS")
print("=" * 100)

for row in high_demand_high_salary:
    print(
        f"{row['skill']:<30}"
        f"Jobs: {row['jobs']:>7,}  "
        f"Demand: {row['demand_pct']:>5.1f}%  "
        f"Median: {row['median_salary']:>6.2f} LPA"
    )


# --------------------------------------------------
# 3. HIGH DEMAND + LOWER SALARY
# --------------------------------------------------

high_demand_lower_salary = [
    row for row in matched_skills
    if row["jobs"] >= demand_threshold
    and row["median_salary"] < salary_threshold
]

high_demand_lower_salary.sort(
    key=lambda row: row["jobs"],
    reverse=True
)

print("\n" + "=" * 100)
print("HIGH DEMAND + RELATIVELY LOWER SALARY")
print("=" * 100)

for row in high_demand_lower_salary:
    print(
        f"{row['skill']:<30}"
        f"Jobs: {row['jobs']:>7,}  "
        f"Demand: {row['demand_pct']:>5.1f}%  "
        f"Median: {row['median_salary']:>6.2f} LPA"
    )


# --------------------------------------------------
# 4. LOWER DEMAND + HIGH SALARY
# --------------------------------------------------

lower_demand_high_salary = [
    row for row in matched_skills
    if row["jobs"] < demand_threshold
    and row["median_salary"] >= salary_threshold
]

lower_demand_high_salary.sort(
    key=lambda row: row["median_salary"],
    reverse=True
)

print("\n" + "=" * 100)
print("RELATIVELY LOWER DEMAND + HIGH SALARY")
print("=" * 100)

for row in lower_demand_high_salary:
    print(
        f"{row['skill']:<30}"
        f"Jobs: {row['jobs']:>7,}  "
        f"Demand: {row['demand_pct']:>5.1f}%  "
        f"Median: {row['median_salary']:>6.2f} LPA"
    )


# --------------------------------------------------
# 5. LOWER DEMAND + LOWER SALARY
# --------------------------------------------------

lower_demand_lower_salary = [
    row for row in matched_skills
    if row["jobs"] < demand_threshold
    and row["median_salary"] < salary_threshold
]

lower_demand_lower_salary.sort(
    key=lambda row: row["jobs"],
    reverse=True
)

print("\n" + "=" * 100)
print("RELATIVELY LOWER DEMAND + LOWER SALARY")
print("=" * 100)

for row in lower_demand_lower_salary:
    print(
        f"{row['skill']:<30}"
        f"Jobs: {row['jobs']:>7,}  "
        f"Demand: {row['demand_pct']:>5.1f}%  "
        f"Median: {row['median_salary']:>6.2f} LPA"
    )


# --------------------------------------------------
# 6. FINAL SUMMARY
# --------------------------------------------------

print("\n" + "=" * 100)
print("ANALYSIS SUMMARY")
print("=" * 100)

print(f"Total salary skills: {len(skill_salaries)}")
print(f"Successfully matched: {len(matched_skills)}")
print(f"Demand threshold: {demand_threshold:,} jobs")
print(f"Salary threshold: {salary_threshold:.2f} LPA")

print("\nANALYSIS COMPLETE")