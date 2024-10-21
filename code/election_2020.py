import csv
import os

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report.csv")


def count_votes(path):
    """Counts votes from the CSV file by state and candidate for 2020."""
    counts = {}

    
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            year = row["year"]
            if year != "2020":  
                continue
            
            state = row["state_po"]
            candidate = row["candidate"]
            votes_str = row["candidatevotes"]

            
            if votes_str == 'NA':
                continue  
            
            try:
                votes = int(votes_str)
            except ValueError:
                
                continue
            
            key = (state, candidate)
            if key in counts:
                counts[key] += votes
            else:
                counts[key] = votes
    
    return counts



def get_rows(counts):
    """Converts the vote counts dictionary into a list of rows."""
    rows = []
    
    for (state, candidate), votes in counts.items():
        rows.append({
            "year": 2020,
            "state_code": state,
            "candidate": candidate,
            "votes": votes
        })
    
    return rows


def sort_rows(rows):
    """Sorts the rows lexicographically by state code and then by votes in descending order."""
    
    rows_lex_ordered = sorted(rows, key=lambda x: (-x["votes"], x["state_code"]))
    return rows_lex_ordered


def write_rows(rows):
    """Writes the sorted rows to a CSV file."""
    with open(OUTPUT_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["year", "state_code", "candidate", "votes"])
        writer.writeheader()  
        writer.writerows(rows)  


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    
    counts = count_votes(IN_PATH)

    
    rows = get_rows(counts)

    
    sorted_rows = sort_rows(rows)

    
    write_rows(sorted_rows)
