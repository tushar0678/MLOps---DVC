import pandas as pd
import os

# Create a sample DataFrame with column names
data = {'Name': ['Ramesh', 'Mohit', 'Ashish'],
    'Age': [25, 30, 35],
    'City': ['Agra', 'Noida', 'Mathura']
    }

df = pd.DataFrame(data)

# # Adding new row to df for V2
new_row_loc = {'Name': 'Rani', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for V3
new_row_loc2 = {'Name': 'Rekha', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2

# Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")