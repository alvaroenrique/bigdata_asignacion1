import happybase
import time

start_time = time.time()

def main():
    conection = happybase.Connection('127.0.0.1')
    table = conection.table('videogames')
    result = {}

    for _, data in table.scan(filter="MultipleColumnPrefixFilter ('data','Year','sales','Global_Sales')"):
        total = result.get(data[b'data:Year'],0) + float(data[b'sales:Global_Sales'].decode("utf-8"))
        result[data[b'data:Year']] = total
    print(result)

if __name__ == "__main__":
    main()
    print("--- Tiempo de procesamiento: %s segundos ---" % (time.time() - start_time))