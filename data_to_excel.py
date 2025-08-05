#!/usr/bin/env python3
"""
Script to convert training data to Excel format.
Usage: Copy your data into the 'data' variable and run the script.
"""

import pandas as pd
import ast
import sys
from typing import List, Tuple, Dict, Any

def parse_data_to_excel(data_string: str, output_filename: str = "training_data.xlsx"):
    """
    Parse the training data string and convert to Excel format.
    
    Args:
        data_string (str): String representation of the data
        output_filename (str): Name of the output Excel file
    """
    try:
        # Parse the string as Python literal
        parsed_data = ast.literal_eval(data_string)
        
        # Convert to list of dictionaries for DataFrame
        rows = []
        for step, metrics in parsed_data:
            row = {'step': step}
            row.update(metrics)
            rows.append(row)
        
        # Create DataFrame
        df = pd.DataFrame(rows)
        
        # Write to Excel
        df.to_excel(output_filename, index=False)
        print(f"Data successfully exported to {output_filename}")
        print(f"Exported {len(rows)} rows with columns: {list(df.columns)}")
        
        # Display preview
        print("\nPreview of the data:")
        print(df.head())
        
    except Exception as e:
        print(f"Error processing data: {e}")
        print("Please check that your data is properly formatted.")

def main():
    # PASTE YOUR DATA HERE
    # Replace the data below with your actual data
    data = """[(499,
  {'time_sample_batch': 0.008892416954040527,
   'time_algorithm_update': 0.008547663688659668,
   'loss': 12.986920356750488,
   'td_loss': 12.61032485961914,
   'conservative_loss': 0.6847189664840698,
   'time_step': 0.017713427543640137}),
 (500,
  {'time_sample_batch': 0.007868528366088867,
   'time_algorithm_update': 0.00818932056427002,
   'loss': 12.809900283813477,
   'td_loss': 12.437970638275146,
   'conservative_loss': 0.6762363910675049,
   'time_step': 0.01625967025756836})]"""
    
    # You can also specify a custom output filename
    output_file = "training_metrics.xlsx"
    
    parse_data_to_excel(data, output_file)

if __name__ == "__main__":
    main()