import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Try loading the CSV file
try:
    df = pd.read_csv("File.CSV.txt")
    print("Dataset loaded successfully.\n")

    # Task 1: Explore the Dataset
    print("First five rows of the dataset:")
    print(df.head())

    print("\nData types and missing values:")
    print(df.info())
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Optional: Clean missing data
    df = df.dropna()

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Task 2: Basic Data Analysis
    print("\nBasic statistics:")
    print(df.describe())

    print("\nAverage sales per region:")
    grouped_region = df.groupby('Region')['Sales'].mean()
    print(grouped_region)

    print("\nTotal sales per product:")
    grouped_product = df.groupby('Product')['Sales'].sum()
    print(grouped_product)

    # Task 3: Data Visualization
    plt.figure(figsize=(16, 12))

    # Line chart: Sales over time
    plt.subplot(2, 2, 1)
    plt.plot(df['Date'], df['Sales'], marker='o')
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.grid(True)

    # Bar chart: Average sales per region
    plt.subplot(2, 2, 2)
    grouped_region.plot(kind='bar', color='skyblue')
    plt.title('Average Sales per Region')
    plt.xlabel('Region')
    plt.ylabel('Average Sales')

    # Histogram: Distribution of sales
    plt.subplot(2, 2, 3)
    plt.hist(df['Sales'], bins=10, color='lightgreen', edgecolor='black')
    plt.title('Sales Distribution')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')

    # Scatter plot: Sales vs Date colored by Region
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df, x='Date', y='Sales', hue='Region')
    plt.title('Sales by Date and Region')
    plt.xlabel('Date')
    plt.ylabel('Sales')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: Could not find 'file.csv'. Please check the file path.")
except pd.errors.ParserError:
    print("Error: Could not parse the CSV file.")
except Exception as e:
    print(f"Unexpected error: {e}")
