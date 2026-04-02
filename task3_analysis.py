import pandas as pd

def task_3_analyze(csv_input):
    df = pd.read_csv(csv_input)

    # 1. Top 5 or Group by category
    summary = df.groupby('category').agg({
        'score': 'mean',
        'num_comments': 'sum',
        'post_id': 'count'
    }).rename(columns={'post_id': 'story_count', 'score': 'avg_score'})

    print("\n--- category summary ---")
    print(summary)
   

    # Finding Top 5 "Viral" stories based on score and num_comments
    df['engagement'] = df['score'] + df['num_comments']
    top_viral = df.nlargest(5, 'engagement') [['title', 'category', 'score', 'engagement', 'author']]

    print("\n--- Top 5 viral stories ---")
    print(top_viral)
    return summary

if __name__ == "__main__":
    task_3_analyze("data/trends_cleaned.csv")