#!/usr/bin/env python3
"""
Data to CSV Converter (No external dependencies required)
Simply paste your data in the data variable and run!
The CSV file can be opened directly in Excel.
"""

import csv
import ast

# PASTE YOUR DATA HERE (replace the example data below)
data = [(499,
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
   'time_step': 0.01625967025756836})]

# Convert to list of dictionaries
rows = []
for step, metrics in data:
    row = {'step': step}
    row.update(metrics)
    rows.append(row)

# Get all column names
if rows:
    columns = list(rows[0].keys())
    
    # Write to CSV
    output_filename = "training_data.csv"
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"✅ Data exported to {output_filename}")
    print(f"📊 Exported {len(rows)} rows")
    print(f"📋 Columns: {', '.join(columns)}")
    print(f"\n📋 Preview (first few rows):")
    print(f"{','.join(columns)}")
    for i, row in enumerate(rows[:5]):  # Show first 5 rows
        values = [str(row[col]) for col in columns]
        print(f"{','.join(values)}")
    
    print(f"\n💡 You can open '{output_filename}' directly in Excel!")
    print("💡 Alternatively, use 'Import Data' in Excel and choose 'Comma Separated Values'")
else:
    print("❌ No data found to export")