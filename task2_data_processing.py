import pandas as pd

def task_2_clean(json_input):
    print("cleaning data...")
    # Load the JSON into a DataFrame
    df = pd.read_json(json_input)

    # Fill missing values with defaults
    df['score'] = df['score'].fillna(0)
    df['num_comments'] = df['num_comments'].fillna(0)

    # Clean title by removing extra whitespaces
    df['title'] = df['title'].str.strip()

    # Save cleaned data to CSV
    output_csv = "data/trends_cleaned.csv"
    df.to_csv(output_csv, index=False)
    print(f"cleaned data saved to {output_csv}")
    return output_csv
if __name__ == "__main__":
    # Example input json file from task1
    import glob
    latest_json = max(glob.glob("data/trends_*.json()"))
    task_2_clean(latest_json)