import pandas as pd
data = pd.read_csv(r'C:\Users\USER430\Documents\giants.csv')
df = pd.DataFrame(data, columns=['CEO', "Established"])
print(df)
