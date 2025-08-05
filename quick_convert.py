#!/usr/bin/env python3
"""
Quick Data to Excel Converter
Simply paste your data in the data variable and run!
"""

import pandas as pd
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

# Convert to DataFrame
rows = []
for step, metrics in data:
    row = {'step': step}
    row.update(metrics)
    rows.append(row)

df = pd.DataFrame(rows)

# Save to Excel
output_filename = "data_output.xlsx"
df.to_excel(output_filename, index=False)

print(f"✅ Data exported to {output_filename}")
print(f"📊 Exported {len(rows)} rows")
print(f"📋 Columns: {', '.join(df.columns)}")
print("\n📋 Preview:")
print(df.to_string(index=False))