India Tech Job Market Analytics (2026)

Project Overview

India Tech Job Market Analytics (2026) is a data analytics project that explores technology skill demand, salary benchmarks, and experience-based salary trends in India's technology job market.

The project uses job-market datasets collected from Jobspiq, with an October 2026 snapshot, to identify highly demanded technical skills, compare salary benchmarks across experience levels and technology roles, and explore the relationship between skill demand and median salary.

Objectives

- Identify the most demanded technical skills in India.
- Analyze salary distribution across experience levels.
- Compare median salaries across technology role families.
- Examine salary benchmarks associated with different technical skills.
- Compare skill demand against median salary.
- Present findings through an interactive-style Excel dashboard.

Tools and Technologies

- Python
- Pandas
- Data Analysis and Exploratory Data Analysis (EDA)
- Matplotlib
- Excel
- Git and GitHub

Dataset Information

The project uses two datasets:

1. Skills Demand Dataset
   
   - Contains technology skill demand information.
   - Demand observation window: 30 days.

2. Tech Salaries Dataset
   
   - Contains stated salary benchmark information.
   - Salary observation window: 90 days.

Data snapshot: October 18, 2026.

Source: Jobspiq.

Note: The datasets represent aggregated job-market information and stated salary benchmarks, not verified individual employment or salary records.

Project Workflow

1. Data Collection
2. Data Inspection
3. Data Quality and Structural Audit
4. Exploratory Data Analysis
5. Salary Analysis
6. Experience-Level Salary Analysis
7. Skill-Based Salary Analysis
8. Skill Demand vs Salary Comparison
9. Data Visualization
10. Excel Dashboard Development

Key Findings

1. Most Demanded Technical Skills

- Python: 20,331 job postings (29.4%)
- SQL: 14,615 job postings (21.2%)
- CI/CD: 13,985 job postings (20.3%)
- AWS: 12,923 job postings (18.7%)
- Azure: 11,930 job postings (17.3%)

2. Salary by Experience

Experience| Median Salary
0–1 years| ₹5.5 LPA
2–4 years| ₹13 LPA
5–8 years| ₹21.5 LPA
9+ years| ₹29.8 LPA

3. Overall Salary Benchmark

- Salary sample size: 504
- Overall median salary: ₹15 LPA
- First quartile (Q1): ₹7 LPA
- Third quartile (Q3): ₹26.6 LPA

4. Salary by Technical Skills

- LLMs: ₹21.8 LPA
- GCP: ₹21.5 LPA
- AWS: ₹19 LPA
- CI/CD: ₹19 LPA
- Azure: ₹19 LPA

These are observed median salary associations, not evidence that a particular skill causes higher compensation.

Dashboard and Visualizations

The Excel dashboard includes eight visualizations:

1. Top 15 Most Demanded Tech Skills in India
2. Median Salary by Experience Level
3. Salary Distribution by Experience Level
4. Top Skills by Median Salary
5. Skill Demand vs Median Salary
6. Median Salary Comparison by Tech Role Family
7. Salary Growth Across Experience Levels
8. Top 5 Most Demanded Tech Skills

The dashboard also includes four KPI cards and five key insights.

Project Structure

JobMarket_Analytics/
│
├── data/
│   └── raw/
│       ├── skills-demand-india.csv
│       ├── tech-salaries-stated-india.csv
│       └── dataset.csv
│
├── inspect_data.py
├── audit_data.py
├── eda.py
├── salary_analysis.py
├── salary_experience.py
├── skill_salary_analysis.py
│
├── India_Tech_Job_Market_Analytics_2026.xlsx
│
└── README.md

Limitations

- The analysis is based on an October 2026 data snapshot.
- Skills demand and stated salary datasets have different observation windows.
- Skill-demand percentages can overlap because one job posting may require multiple skills.
- Salary benchmarks are based on stated salary data and may not represent actual compensation.
- Relationships between skills and salaries should not be interpreted as causal relationships.
- Demand-versus-salary categories use project-defined comparison thresholds, not official industry classifications.

Conclusion

This project demonstrates how Python-based data analysis and Excel visualization can be used to explore technology job-market trends.

It provides insights into in-demand technical skills, salary benchmarks, experience-based compensation patterns, and the relationship between skill demand and salary.

The project also demonstrates practical skills in data cleaning, exploratory analysis, statistical summaries, visualization, and dashboard development.

Author

Ishwarya R Karajola

Data Analytics Project | 2026