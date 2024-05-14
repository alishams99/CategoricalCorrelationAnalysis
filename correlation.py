import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

excel_file_path = 'balance_data.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='Sheet1')
categorical_columns = [
    'Location', 'Province', 'Occupation', 'Employment Status',
    'Gender', 'Day vs Night', 'Activity', 'Incident Type', 'Classification'
]

for i in categorical_columns :
    contingency_table = pd.crosstab(df[i], df['Nature of injury'])

    chi2, _, _, _ = chi2_contingency(contingency_table)
    n = df.shape[0]
    min_dim = min(contingency_table.shape) - 1
    cramers_v = np.sqrt(chi2 / (n * min_dim))

    print(f"correlation's {i}: {cramers_v}")
    
