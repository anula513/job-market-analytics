import pandas as pd

# load raw data
df = pd.read_csv("data/raw/jobs_raw.csv")

# standardize column names
df.columns = df.columns.str.strip().str.lower()

# remove duplicate rows
df = df.drop_duplicates()

# drop rows missing key fields
df = df.dropna(subset=["job_title", "experience_level", "salary_in_usd", "company_location"])

# clean text columns
df["job_title"] = df["job_title"].astype(str).str.strip()
df["experience_level"] = df["experience_level"].astype(str).str.strip().str.upper()
df["employment_type"] = df["employment_type"].astype(str).str.strip().str.upper()
df["company_location"] = df["company_location"].astype(str).str.strip().str.upper()
df["employee_residence"] = df["employee_residence"].astype(str).str.strip().str.upper()
df["company_size"] = df["company_size"].astype(str).str.strip().str.upper()

# convert numeric columns
df["work_year"] = pd.to_numeric(df["work_year"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["salary_in_usd"] = pd.to_numeric(df["salary_in_usd"], errors="coerce")
df["remote_ratio"] = pd.to_numeric(df["remote_ratio"], errors="coerce")

# keep only valid remote ratios
df = df[df["remote_ratio"].isin([0, 50, 100])]

# remove invalid salaries
df = df[df["salary_in_usd"] > 0]

# optional: map short experience codes to readable labels
experience_map = {
    "EN": "Entry-level",
    "MI": "Mid-level",
    "SE": "Senior-level",
    "EX": "Executive-level"
}
df["experience_label"] = df["experience_level"].map(experience_map)

# save cleaned data
df.to_csv("data/cleaned/jobs_cleaned.csv", index=False)

print("Cleaning complete.")
print(f"Rows after cleaning: {len(df)}")
print("Cleaned file saved to data/cleaned/jobs_cleaned.csv")