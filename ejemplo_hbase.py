import happybase

def main():
    conection = happybase.Connection('127.0.0.1')
    tb_alumno = conection.table('alumno')

    """ tb_alumno.put(b'20151932', {
        b'dp:nombre': b'asdfasdf'
    }) """

    row = tb_alumno.row(b'20151932')
    print(row[b"dp:nombre"])

    conection.close()

if __name__ == "__main__":
    main()