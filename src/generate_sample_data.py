"""
Sample Data Generator
Generates sample data for testing the ETL pipeline
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)


def generate_sample_sales_data(num_rows: int = 1000) -> pd.DataFrame:
    """
    Generate sample sales data
    
    Args:
        num_rows: Number of rows to generate
        
    Returns:
        DataFrame with sample sales data
    """
    # Generate dates
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(num_rows)]
    
    # Generate product categories
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Home']
    
    # Generate data
    data = {
        'transaction_id': range(1, num_rows + 1),
        'date': dates,
        'product_category': [random.choice(categories) for _ in range(num_rows)],
        'product_name': [f'Product_{random.randint(1, 100)}' for _ in range(num_rows)],
        'quantity': np.random.randint(1, 10, num_rows),
        'unit_price': np.round(np.random.uniform(10, 500, num_rows), 2),
        'customer_id': [f'CUST_{random.randint(1, 200):04d}' for _ in range(num_rows)],
        'region': [random.choice(['North', 'South', 'East', 'West']) for _ in range(num_rows)],
    }
    
    df = pd.DataFrame(data)
    
    # Calculate total price
    df['total_price'] = df['quantity'] * df['unit_price']
    
    # Add some duplicates (5%)
    num_duplicates = int(num_rows * 0.05)
    duplicate_indices = np.random.choice(df.index, num_duplicates, replace=False)
    duplicates = df.loc[duplicate_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # Add some missing values (3%)
    for col in ['quantity', 'unit_price', 'customer_id']:
        missing_indices = np.random.choice(df.index, int(len(df) * 0.03), replace=False)
        df.loc[missing_indices, col] = np.nan
    
    return df


def save_sample_data(output_dir: str = "data/raw"):
    """
    Generate and save sample data
    
    Args:
        output_dir: Directory to save the sample data
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate sales data
    sales_data = generate_sample_sales_data(1000)
    sales_file = os.path.join(output_dir, "sample_data.csv")
    sales_data.to_csv(sales_file, index=False)
    print(f"Sample sales data saved to: {sales_file}")
    print(f"Generated {len(sales_data)} rows with {len(sales_data.columns)} columns")
    
    # Display sample
    print("\nSample data preview:")
    print(sales_data.head())
    print(f"\nData info:")
    print(sales_data.info())
    print(f"\nMissing values:")
    print(sales_data.isnull().sum())


if __name__ == "__main__":
    save_sample_data()
