import pandas as pd
data=pd.read_csv("nba",index_col="name")
first=data[["Age","College","Salary"]]
print(first)