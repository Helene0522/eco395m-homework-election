import csv
import os

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report.csv")


def count_votes(path):
    """Counts votes from the CSV file by state and candidate for 2020."""
    counts = {}

    # Open the input CSV file and read its contents
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            year = row["year"]
            if year != "2020":  # Only process rows for the year 2020
                continue
            
            state = row["state_po"]
            candidate = row["candidate"]
            votes_str = row["candidatevotes"]

            # 处理 NA 值，忽略这些行或将其视为 0
            if votes_str == 'NA':
                continue  # 跳过该行，如果 votes 为 'NA'
            
            try:
                votes = int(votes_str)
            except ValueError:
                # 如果无法转换为整数，则跳过该行
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
    # Sort first by votes in descending order, then by state code in alphabetical order
    rows_lex_ordered = sorted(rows, key=lambda x: (-x["votes"], x["state_code"]))
    return rows_lex_ordered


def write_rows(rows):
    """Writes the sorted rows to a CSV file."""
    with open(OUTPUT_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["year", "state_code", "candidate", "votes"])
        writer.writeheader()  # Write the CSV header
        writer.writerows(rows)  # Write all the rows


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Step 1: Count votes
    counts = count_votes(IN_PATH)

    # Step 2: Convert counts to rows
    rows = get_rows(counts)

    # Step 3: Sort rows
    sorted_rows = sort_rows(rows)

    # Step 4: Write rows to CSV
    write_rows(sorted_rows)
