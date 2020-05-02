import happybase
import time
import operator

start_time = time.time()

def main():
    conection = happybase.Connection('127.0.0.1')
    table = conection.table('videogames')
    result = {}

    for _, data in table.scan(filter="MultipleColumnPrefixFilter ('data','Platform','sales','Global_Sales')"):
        total = result.get(data[b'data:Platform'],0) + float(data[b'sales:Global_Sales'].decode("utf-8"))
        result[data[b'data:Platform']] = total
    print(result)
    print("-----> ")
    print(max(result.items(), key=operator.itemgetter(1))[0])

if __name__ == "__main__":
    main()
    print("--- Tiempo de procesamiento: %s segundos ---" % (time.time() - start_time))