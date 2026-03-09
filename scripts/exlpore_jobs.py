import pandas as pd

# load dataset
df = pd.read_csv("data/raw/jobs_raw.csv")

# show first rows
print("\nFIRST 5 ROWS:")
print(df.head())

# dataset info
print("\nDATASET INFO:")
print(df.info())

# basic statistics
print("\nSUMMARY STATISTICS:")
print(df.describe())

# unique job titles
print("\nTOP JOB TITLES:")
print(df["job_title"].value_counts().head(10))

# experience levels
print("\nEXPERIENCE LEVEL COUNTS:")
print(df["experience_level"].value_counts())

# remote ratio distribution
print("\nREMOTE RATIO DISTRIBUTION:")
print(df["remote_ratio"].value_counts())