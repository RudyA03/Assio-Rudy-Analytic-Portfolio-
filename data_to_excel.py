#!/usr/bin/env python3
"""
Script to convert data from list of tuples format to Excel file.
Usage: Paste your data into the 'data' variable and run the script.
"""

import pandas as pd
import ast
from typing import List, Tuple, Dict, Any

def data_to_excel(data: List[Tuple[int, Dict[str, float]]], output_file: str = "output.xlsx"):
    """
    Convert list of tuples data to Excel file.
    
    Args:
        data: List of tuples where each tuple contains (index, dict_of_metrics)
        output_file: Name of the output Excel file
    """
    # Extract data into a list of dictionaries for easier DataFrame creation
    rows = []
    for index, metrics in data:
        row = {'index': index}
        row.update(metrics)
        rows.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(rows)
    
    # Save to Excel
    df.to_excel(output_file, index=False)
    print(f"Data successfully saved to {output_file}")
    print(f"Shape: {df.shape}")
    print("\nColumn names:")
    for col in df.columns:
        print(f"  - {col}")

def parse_data_string(data_string: str) -> List[Tuple[int, Dict[str, float]]]:
    """
    Parse a string representation of the data into the actual data structure.
    
    Args:
        data_string: String representation of the data
        
    Returns:
        Parsed data structure
    """
    try:
        # Use ast.literal_eval for safe evaluation
        return ast.literal_eval(data_string)
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing data: {e}")
        print("Please ensure your data is in valid Python format.")
        return []

if __name__ == "__main__":
    # PASTE YOUR DATA HERE - Replace this with your actual data
    data_string = """[(1,
  {'time_sample_batch': 0.0059969425201416016,
   'time_algorithm_update': 0.010038971900939941,
   'loss': 3.1598966121673584,
   'td_loss': 2.7928504943847656,
   'conservative_loss': 0.6673566699028015,
   'time_step': 0.016215085983276367}),
 (2,
  {'time_sample_batch': 0.0071364641189575195,
   'time_algorithm_update': 0.007921457290649414,
   'loss': 3.1699254512786865,
   'td_loss': 2.8481216430664062,
   'conservative_loss': 0.5850978493690491,
   'time_step': 0.015322089195251465}),
 (3,
  {'time_sample_batch': 0.005462527275085449,
   'time_algorithm_update': 0.006604433059692383,
   'loss': 3.5267547369003296,
   'td_loss': 3.1523025035858154,
   'conservative_loss': 0.6808221936225891,
   'time_step': 0.012259364128112793}),
 (4,
  {'time_sample_batch': 0.006090521812438965,
   'time_algorithm_update': 0.007620453834533691,
   'loss': 4.934777736663818,
   'td_loss': 4.565727233886719,
   'conservative_loss': 0.671000748872757,
   'time_step': 0.013910412788391113}),
 (5,
  {'time_sample_batch': 0.006775498390197754,
   'time_algorithm_update': 0.006739497184753418,
   'loss': 6.34333872795105,
   'td_loss': 5.838082313537598,
   'conservative_loss': 0.9186479449272156,
   'time_step': 0.01369786262512207}),
 (6,
  {'time_sample_batch': 0.006728529930114746,
   'time_algorithm_update': 0.0058449506759643555,
   'loss': 7.8852314949035645,
   'td_loss': 7.221906900405884,
   'conservative_loss': 1.2060444355010986,
   'time_step': 0.01281893253326416}),
 (7,
  {'time_sample_batch': 0.005873441696166992,
   'time_algorithm_update': 0.006693482398986816,
   'loss': 10.702649593353271,
   'td_loss': 9.686820030212402,
   'conservative_loss': 1.846962571144104,
   'time_step': 0.012758016586303711}),
 (8,
  {'time_sample_batch': 0.005822539329528809,
   'time_algorithm_update': 0.006977558135986328,
   'loss': 12.928144931793213,
   'td_loss': 11.974629402160645,
   'conservative_loss': 1.7336646914482117,
   'time_step': 0.013003945350646973}),
 (9,
  {'time_sample_batch': 0.006672501564025879,
   'time_algorithm_update': 0.006678104400634766,
   'loss': 11.148264408111572,
   'td_loss': 9.996308326721191,
   'conservative_loss': 2.0944656133651733,
   'time_step': 0.013546943664550781}),
 (10,
  {'time_sample_batch': 0.007378697395324707,
   'time_algorithm_update': 0.0055779218673706055,
   'loss': 17.364070892333984,
   'td_loss': 16.034062385559082,
   'conservative_loss': 2.418197512626648,
   'time_step': 0.013213396072387695}),
 (11,
  {'time_sample_batch': 0.005685925483703613,
   'time_algorithm_update': 0.006517767906188965,
   'loss': 17.45364761352539,
   'td_loss': 15.817341804504395,
   'conservative_loss': 2.9751017093658447,
   'time_step': 0.012379050254821777})]"""
    
    # Parse the data
    parsed_data = parse_data_string(data_string)
    
    if parsed_data:
        # Convert to Excel
        data_to_excel(parsed_data)
        
        # Also show a preview of the DataFrame
        rows = []
        for index, metrics in parsed_data:
            row = {'index': index}
            row.update(metrics)
            rows.append(row)
        
        df = pd.DataFrame(rows)
        print("\nPreview of the data:")
        print(df.head())
        print("\nData types:")
        print(df.dtypes)
    else:
        print("Failed to parse data. Please check the format.")