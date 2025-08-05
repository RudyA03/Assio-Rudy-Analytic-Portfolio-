# Data to Excel/CSV Converter

This repository contains Python scripts to convert training data (tuples with dictionaries) into Excel or CSV format.

## Files Included

1. **`data_to_csv.py`** - ✅ **Recommended** (No dependencies required)
2. **`quick_convert.py`** - Requires pandas and openpyxl
3. **`data_to_excel.py`** - Full-featured version with error handling
4. **`requirements.txt`** - Dependencies for pandas-based scripts

## Quick Start (Recommended)

### Option 1: CSV Output (No Dependencies)

1. Open `data_to_csv.py`
2. Replace the `data` variable with your data
3. Run: `python3 data_to_csv.py`
4. Open the generated `training_data.csv` in Excel

```python
# Replace this data with yours:
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
```

### Option 2: Direct Excel Output (Requires Dependencies)

1. Install dependencies: `pip install pandas openpyxl`
2. Open `quick_convert.py`
3. Replace the `data` variable with your data
4. Run: `python3 quick_convert.py`
5. Open the generated `data_output.xlsx`

## Data Format

Your data should be in this format:
```python
[(step_number, {metric_dict}), (step_number, {metric_dict}), ...]
```

Example:
```python
[(499, {'loss': 12.98, 'time': 0.008}), (500, {'loss': 12.80, 'time': 0.007})]
```

## Output

The scripts will create a table with:
- `step` column (from the tuple's first element)
- One column for each metric in the dictionaries

Example output:
| step | time_sample_batch | time_algorithm_update | loss | td_loss | conservative_loss | time_step |
|------|-------------------|----------------------|------|---------|-------------------|-----------|
| 499  | 0.008892         | 0.008548            | 12.987| 12.610  | 0.684719         | 0.017713  |
| 500  | 0.007869         | 0.008189            | 12.810| 12.438  | 0.676236         | 0.016260  |

## Usage Tips

- Simply copy and paste your data into the `data` variable
- The CSV version works with any Python installation
- CSV files can be opened directly in Excel, Google Sheets, etc.
- For true Excel files (.xlsx), use the pandas-based scripts 
