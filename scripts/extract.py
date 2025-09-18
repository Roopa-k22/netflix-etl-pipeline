import pandas as pd

def extract_data(file_path):
    """Read raw Netflix CSV dataset"""
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} rows and {len(df.columns)} columns")
    return df

if __name__ == "__main__":
    raw_file = "../data/raw/netflix_titles.csv"
    df = extract_data(raw_file)
