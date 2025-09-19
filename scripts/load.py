import pandas as pd
import sqlite3

def load_to_sqlite(csv_file, db_file="netflix.db", table_name="netflix"):
    """Load processed CSV into SQLite database"""
    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Loaded {len(df)} rows into SQLite table '{table_name}' in {db_file}")

if __name__ == "__main__":
    processed_file = "/Users/roopakrishna/Documents/netflix-etl-pipeline/data/processed/netflix_processed.csv"
    load_to_sqlite(processed_file)
