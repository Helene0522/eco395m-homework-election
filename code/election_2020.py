import csv
import os

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report.csv")


def count_votes(path):

    # you write this

    return counts


def get_rows(counts):

    # you write this

    return rows


def sort_rows(rows):

    # you write this

    return rows_lex_ordered


def write_rows(rows):

    # you write this


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    counts = count_votes(IN_PATH)
    rows = get_rows(counts)
    sorted_rows = sort_rows(rows)
    write_rows(sorted_rows)
