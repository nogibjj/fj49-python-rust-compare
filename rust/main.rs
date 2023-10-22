extern crate csv;
use std::error::Error;
use std::fs::File;

fn main() -> Result<(), Box<dyn Error>> {
    // Open the CSV file
    let file = File::open("https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Cryptocurrency/bitcoin.csv")?;
    let mut rdr = csv::Reader::from_reader(file);

    // Define a struct to represent a row in the CSV
    #[derive(Debug, serde::Deserialize)]
    struct Record {
        Date: String,
        Close: f64,
    }

    // Initialize a vector to store records
    let mut records: Vec<Record> = Vec::new();

    // Read the CSV records
    for result in rdr.deserialize() {
        let record: Record = result?;
        records.push(record);
    }

    // Sort records by the "Close" column in descending order
    records.sort_by(|a, b| b.Close.partial_cmp(&a.Close).unwrap());

    // Print the top 10 dates with the highest "Close" values
    println!("Top 10 Dates with the Highest Close Values:");
    for record in &records[0..10] {
        println!("Date: {}, Close: {:.2}", record.Date, record.Close);
    }

    Ok(())
}
