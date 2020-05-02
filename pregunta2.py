import csv
import happybase

csv_data = 'vgsales.csv'

data = open(csv_data)
reader = csv.DictReader(data)

# Conexión con hbase
conn = happybase.Connection('127.0.0.1')
table = conn.table('videogames')

# Iteración de las filas del csv
for row in reader:
    # Se inserta los datos de la fila en las columnas de hbase (data y sales)
    table.put(row['Rank'].encode(), {'data:Name': row["Name"].encode(), "data:Platform": row["Platform"].encode(),
                                     "data:Year": row["Year"].encode(), "data:Genre": row["Genre"].encode(),
                                     "data:Publisher": row["Publisher"].encode(), "sales:NA_Sales": row["NA_Sales"].encode(),
                                     "sales:EU_Sales": row["EU_Sales"].encode(), "sales:JP_Sales": row["JP_Sales"].encode(),
                                     "sales:Other_Sales": row["Other_Sales"].encode(), "sales:Global_Sales": row["Global_Sales"].encode()})
