import csv
import requests

github_csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Cryptocurrency/bitcoin.csv'

# Lists to store the data
data = []

# Open and read the CSV file from the GitHub URL
try:
    response = requests.get(github_csv_url)
    if response.status_code == 200:
        csv_data = response.text
    else:
        raise Exception("Failed to fetch CSV data")
except Exception as e:
    print(f"Failed to fetch CSV data: {e}")
    exit()

# Create a CSV reader
csv_reader = csv.reader(csv_data.splitlines())

# Skip the header row
header = next(csv_reader)

# Define a function to get the "Close" and "Market Cap" values from a row
def get_values(row):
    return float(row[header.index("Close")]), float(row[header.index("Market Cap")])

# Create a list of dates and corresponding values
date_close_cap_pairs = [(row[0], *get_values(row)) for row in csv_reader]

# Sort the list by "Close" values and "Market Cap" values in descending order
date_close_cap_pairs.sort(key=lambda x: (x[1], x[2]), reverse=True)

# Print the top 10 dates with the highest "Close" values
print("Top 20 Dates with Highest 'Close' Values:")
for i, (date, close, market_cap) in enumerate(date_close_cap_pairs[:20], start=1):
    print(f"{i}. Date: {date}, Close: {close:.2f}, Market Cap: {market_cap:.2f}")
