import happybase
import time

start_time = time.time()

def main():
    conection = happybase.Connection('127.0.0.1')
    table = conection.table('videogames')
    result = {}

    # Por cada recorrido se obtiene el key de las filas, que en este caso es la columna Rank del csv,
    # y un diccionario llamado data que contiene el resultado del query a hbase
    for key, data in table.scan(filter="MultipleColumnPrefixFilter ('data','Year','sales','Global_Sales')"):
        # Al diccionario result se le asinga un nuevo key con un value que se suma cada vez que el key se vuelve a repetir
        total = result.get(data[b'data:Year'],0) + float(data[b'sales:Global_Sales'].decode("utf-8"))
        result[data[b'data:Year']] = total
    print(result)

if __name__ == "__main__":
    main()
    print("--- Tiempo de procesamiento: %s segundos ---" % (time.time() - start_time))