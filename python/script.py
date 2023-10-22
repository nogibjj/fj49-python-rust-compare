import csv

# Replace 'your_github_csv_url' with the actual GitHub raw CSV file URL
github_csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Cryptocurrency/bitcoin.csv'

# Lists to store the data
data = []

# Open and read the CSV file from the GitHub URL
try:
    import requests
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

# Define a function to get the "Close" value from a row
def get_close(row):
    return float(row[header.index("Close")])

# Create a list of dates and corresponding close values
date_close_pairs = [(row[0], get_close(row)) for row in csv_reader]

# Sort the list by close values in descending order
date_close_pairs.sort(key=lambda x: x[1], reverse=True)

# Print the top 10 dates with the highest "Close" values
print("Top 10 Dates with Highest 'Close' Values:")
for i, (date, close) in enumerate(date_close_pairs[:10], start=1):
    print(f"{i}. Date: {date}, Close: {close:.2f}")
