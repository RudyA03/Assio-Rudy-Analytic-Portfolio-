# Data to Excel Converter

This script converts Python data in list of tuples format to Excel files.

## Files

- `data_to_excel.py` - Main conversion script
- `requirements.txt` - Required Python packages
- `output.xlsx` - Example output file (generated when script runs)

## Usage

### Method 1: Replace data in the script
1. Open `data_to_excel.py`
2. Replace the `data_string` variable (around line 57) with your actual data
3. Run the script:
   ```bash
   python3 data_to_excel.py
   ```

### Method 2: Modify the script to use your data directly
You can also modify the script to work with your data programmatically:

```python
from data_to_excel import data_to_excel

# Your data here
your_data = [(1, {'metric1': 1.5, 'metric2': 2.5}), (2, {'metric1': 1.8, 'metric2': 2.1})]

# Convert to Excel
data_to_excel(your_data, "my_output.xlsx")
```

## Data Format

The script expects data in this format:
```python
[(index, {'metric1': value1, 'metric2': value2, ...}), ...]
```

Where:
- `index` is an integer (typically step/iteration number)
- The dictionary contains metric names and their corresponding float values

## Output

The script creates an Excel file with:
- Each row representing one data point
- First column: index values
- Subsequent columns: metric values
- Column headers are automatically generated from the metric names

## Example Data Structure

```python
[(1, {'time_sample_batch': 0.005997, 'loss': 3.159}),
 (2, {'time_sample_batch': 0.007136, 'loss': 3.169})]
```

Becomes an Excel file with columns:
- index
- time_sample_batch  
- loss

## Requirements

- Python 3.x
- pandas
- openpyxl

Install dependencies:
```bash
# On Ubuntu/Debian
sudo apt install python3-pandas python3-openpyxl

# Or using pip (in virtual environment)
pip install pandas openpyxl
``` 
