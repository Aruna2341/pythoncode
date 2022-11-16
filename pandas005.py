import pandas as pd
data = {'Country':['India','Belgium', 'Brazil'],'Capital':['NewDelhi', 'Brasilia','Brussels'],
        'Population':[11190846, 1303171035, 207847528]}
df = pd.DataFrame(data,columns=['Country', 'Capital', 'Population'])
print(df)
