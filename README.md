# Sales Data Analysis and Visualization

This Python script performs exploratory data analysis and visualization on a sales dataset provided in CSV format. It is designed to help users understand sales trends, identify missing data, and generate insightful charts.

## Features

- Loads and validates a CSV file
- Displays basic dataset information and statistics
- Handles missing values
- Converts date strings to datetime objects
- Groups and summarizes sales data by region and product
- Generates four types of visualizations:
  - Line chart of sales over time
  - Bar chart of average sales per region
  - Histogram of sales distribution
  - Scatter plot of sales by date and region

## Requirements

Make sure the following Python libraries are installed:

```bash
pip install pandas numpy matplotlib seaborn
File Format
The script expects a CSV file named File.CSV.txt with the following columns:

Date: Date of the sale (e.g., 2023-07-15)

Region: Sales region (e.g., East, West)

Product: Product name or category

Sales: Numeric sales amount

Usage
Place your CSV file in the same directory as the script and name it File.CSV.txt.

Run the script using Python:

bash
python your_script_name.py
If the file is missing or malformed, the script will print an error message.

If successful, it will display data summaries and open a window with four visualizations.

Error Handling
The script gracefully handles:

Missing file (FileNotFoundError)

Malformed CSV (ParserError)

Other unexpected exceptions

Output
Console output includes data previews, missing value summaries, and grouped statistics.

A matplotlib window displays the four charts for visual analysis.
