import pandas as pd

data = pd.Series([1,2.5, "Hello", [1,2,4]])
print(data)
print(type(data))

df = pd.DataFrame({'name': ['anil', 'sunil', 'ramesh', 'suresh'], 'score':[56,45, 87, 89]})
print(df)
print("_______________________________")
print(df["name"])
print("_______________________________")
print(df["score"])