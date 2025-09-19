import pandas as pd

def transform_data(df):
    """Clean and transform Netflix dataset"""
    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values (simple approach)
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['date_added'] = df['date_added'].fillna('Unknown')

    # Normalize column names to lowercase
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Example filter: only movies after 2010
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
    df = df[df['release_year'] >= 2010]

    print(f"Transformed dataset now has {len(df)} rows")
    return df

if __name__ == "__main__":
    raw_file = "/Users/roopakrishna/Documents/netflix-etl-pipeline/data/raw/netflix_titles.csv"
    processed_file = "/Users/roopakrishna/Documents/netflix-etl-pipeline/data/processed/netflix_processed.csv"

    # Extract first
    df = pd.read_csv(raw_file)

    # Transform
    df_clean = transform_data(df)

    # Save to processed folder
    df_clean.to_csv(processed_file, index=False)
    print(f"Processed file saved at {processed_file}")
