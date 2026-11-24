import csv

FILE_NAME = "data/raw/tech-salaries-stated-india.csv"

experience_order = {
    "0–1 years": 1,
    "2–4 years": 2,
    "5–8 years": 3,
    "9+ years": 4
}

with open(FILE_NAME, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)

experience_data = [
    row for row in data
    if row["group_type"] == "experience"
]

experience_data.sort(
    key=lambda row: experience_order.get(row["group"], 99)
)

# --------------------------------------------------
# 1. SALARY DISTRIBUTION BY EXPERIENCE
# --------------------------------------------------

print("=" * 100)
print("INDIA TECH - SALARY PROGRESSION BY EXPERIENCE")
print("=" * 100)

print(
    f"{'Experience':<18}"
    f"{'Sample':>10}"
    f"{'Q1':>12}"
    f"{'Median':>12}"
    f"{'Q3':>12}"
    f"{'Spread':>12}"
)
print("-" * 100)

for row in experience_data:
    q1 = float(row["lower_quartile_lpa"])
    median = float(row["median_lpa"])
    q3 = float(row["upper_quartile_lpa"])
    spread = q3 - q1

    print(
        f"{row['group']:<18}"
        f"{int(row['stated_salaries']):>10}"
        f"{q1:>12.2f}"
        f"{median:>12.2f}"
        f"{q3:>12.2f}"
        f"{spread:>12.2f}"
    )


# --------------------------------------------------
# 2. MEDIAN SALARY CHANGE BETWEEN EXPERIENCE LEVELS
# --------------------------------------------------

print("\n" + "=" * 100)
print("MEDIAN SALARY CHANGE BETWEEN EXPERIENCE LEVELS")
print("=" * 100)

print(
    f"{'Experience transition':<28}"
    f"{'Previous Median':>18}"
    f"{'New Median':>15}"
    f"{'Increase (LPA)':>18}"
    f"{'Increase (%)':>14}"
)
print("-" * 100)

for i in range(1, len(experience_data)):
    previous = experience_data[i - 1]
    current = experience_data[i]

    previous_median = float(previous["median_lpa"])
    current_median = float(current["median_lpa"])

    increase = current_median - previous_median
    increase_pct = (increase / previous_median) * 100

    transition = f"{previous['group']} -> {current['group']}"

    print(
        f"{transition:<28}"
        f"{previous_median:>18.2f}"
        f"{current_median:>15.2f}"
        f"{increase:>18.2f}"
        f"{increase_pct:>13.2f}%"
    )


# --------------------------------------------------
# 3. SALARY COMPARISON WITH ENTRY-LEVEL BENCHMARK
# --------------------------------------------------

print("\n" + "=" * 100)
print("SALARY COMPARISON RELATIVE TO 0-1 YEARS EXPERIENCE")
print("=" * 100)

if experience_data:
    entry_level_median = float(
        experience_data[0]["median_lpa"]
    )

    print(f"Entry-level median benchmark: {entry_level_median:.2f} LPA\n")

    print(
        f"{'Experience':<18}"
        f"{'Median Salary':>18}"
        f"{'Increase (LPA)':>18}"
        f"{'Growth (%)':>14}"
    )
    print("-" * 70)

    for row in experience_data:
        median = float(row["median_lpa"])
        increase = median - entry_level_median
        growth = (increase / entry_level_median) * 100

        print(
            f"{row['group']:<18}"
            f"{median:>18.2f}"
            f"{increase:>18.2f}"
            f"{growth:>13.2f}%"
        )


# --------------------------------------------------
# 4. EXPERIENCE WITH WIDEST SALARY RANGE
# --------------------------------------------------

print("\n" + "=" * 100)
print("SALARY VARIATION BY EXPERIENCE")
print("=" * 100)

widest = max(
    experience_data,
    key=lambda row: (
        float(row["upper_quartile_lpa"])
        - float(row["lower_quartile_lpa"])
    )
)

widest_spread = (
    float(widest["upper_quartile_lpa"])
    - float(widest["lower_quartile_lpa"])
)

print(f"Widest salary spread: {widest['group']}")
print(f"Q1: {float(widest['lower_quartile_lpa']):.2f} LPA")
print(f"Q3: {float(widest['upper_quartile_lpa']):.2f} LPA")
print(f"Spread: {widest_spread:.2f} LPA")

print("\nSALARY EXPERIENCE ANALYSIS COMPLETE")