import os
import pandas as pd

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report_pandas.csv")

if __name__ == "__main__":
    # Step 1: Read data
    df = pd.read_csv(IN_PATH)
    
    # Step 2: Filter for the year 2020
    df_2020 = df[df["year"] == 2020]
    
    # Step 3: Group by state and candidate, and sum the votes
    grouped = df_2020.groupby(["state_po", "candidate"], as_index=False)["candidatevotes"].sum()
    
    # Step 4: Rename columns for clarity
    grouped.rename(columns={"state_po": "state_code", "candidatevotes": "votes"}, inplace=True)
    
    # Step 5: Sort by state_code alphabetically and votes in descending order
    grouped = grouped.sort_values(by=["state_code", "votes"], ascending=[True, False])
    
    # Step 6: Add the year column
    grouped["year"] = 2020
    
    # Step 7: Reorder the columns
    grouped = grouped[["year", "state_code", "candidate", "votes"]]
    
    # Step 8: Write the result to a CSV file
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    grouped.to_csv(OUTPUT_PATH, index=False)
