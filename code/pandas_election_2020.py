import os
import pandas as pd

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report_pandas.csv")

if __name__ == "__main__":
    
    df = pd.read_csv(IN_PATH)
    
    
    df_2020 = df[df["year"] == 2020]
    
    
    grouped = df_2020.groupby(["state_po", "candidate"], as_index=False)["candidatevotes"].sum()
    
    
    grouped.rename(columns={"state_po": "state_code", "candidatevotes": "votes"}, inplace=True)
    
    
    grouped = grouped.sort_values(by=["state_code", "votes"], ascending=[True, False])
    
    
    grouped["year"] = 2020
    
    
    grouped = grouped[["year", "state_code", "candidate", "votes"]]
    
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    grouped.to_csv(OUTPUT_PATH, index=False)
