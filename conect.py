import pyodbc

server = 'localhost\\SQLEXPRESS'
database = 'Club_Voleibol'
trusted_connection = 'yes'

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection={trusted_connection};'
)

try:
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            print("Conexión exitosa, ejecutando consulta...")
            cursor.execute("SELECT * FROM Deportistas")
            rows = cursor.fetchall()

            if not rows:
                print("No se encontraron registros en la tabla Deportistas.")
            else:
                for row in rows:
                    print(row)

except pyodbc.Error as e:
    print("Error al conectar o ejecutar consulta:", e)
