import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_csv("data/cleaned/jobs_cleaned.csv")

# remove id if it somehow exists
if "id" in df.columns:
    df = df.drop(columns=["id"])

# optional: clear old rows before reloading
with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE jobs RESTART IDENTITY;"))
    conn.commit()

df.to_sql("jobs", engine, if_exists="append", index=False)

print("Data loaded successfully into PostgreSQL!")
print(f"Rows inserted: {len(df)}")