
import pandas as pd

df = pd.read_csv('cities.csv')
df.head()

html_table = df.to_html()


df.to_html('table.html')