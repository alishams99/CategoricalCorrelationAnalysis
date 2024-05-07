# CategoricalCorrelationAnalysis
This repository contains a Python script for performing categorical correlation analysis on an Excel dataset. The script utilizes pandas, scipy, and numpy libraries for data manipulation and statistical analysis.

## Script

- **categorical_correlation_analysis.py**: This script reads an Excel file (`balance_data.xlsx`) containing categorical and nature of injury data. It calculates the Cramer's V correlation coefficient between each categorical column and the 'Nature of injury' column. The results are printed to the console.

## Usage

1. Clone this repository to your local machine using `git clone https://github.com/alishams99/CategoricalCorrelationAnalysis.git`.
2. Ensure you have Python installed on your machine.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Adjust the `excel_file_path` variable in the script to point to your Excel file if necessary.
5. Run the script using Python.

## Example Output

The script calculates the Cramer's V correlation coefficient for each categorical column in the dataset. Below is an example of the output:

```
correlation's Location: 0.342
correlation's Province: 0.512
correlation's Occupation: 0.212
correlation's Employment Status: 0.187
correlation's Gender: 0.097
correlation's Day vs Night: 0.132
correlation's Activity: 0.287
correlation's Incident Type: 0.415
correlation's Classification: 0.223
```

## Data

The provided dataset (`balance_data.xlsx`) contains a sample of 1000 rows of data. Please note that this is a small subset of the actual dataset, and the correlation coefficients may vary with larger datasets.

