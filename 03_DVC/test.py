import pandas as pd 
import os   

data = pd.DataFrame({
    'name': ['John', 'Jane', 'Bob', 'Alice'],
    'age': [25, 30, 35, 40],
    'city': ['New York', 'Paris', 'London', 'Tokyo']
})


data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "data.csv")
data.to_csv(file_path, index=False)

print("Data saved to", file_path)