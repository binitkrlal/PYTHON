import pandas as pd

data = {
    "Name": ["Binit", "Rahul", "Aman"],
    "Age": [22, 23, 21],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)