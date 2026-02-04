import pandas as pd
import os

data = {'Name':['Kushal', 'Ankit', 'Suresh'],
        'Age':[25, 30, 22],
        'City':['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'data.csv')
df.to_csv(file_path, index=False)
print(f"CSV saved to {file_path}")
print(df)