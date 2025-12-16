import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100),edad INTERGER, email VARCHAR(100))")
#cursor.execute("INSERT INTO usuarios VALUES ('Hector',27,'hecto@ejemplo.com')")
# usuarios = [
# ('Loco',56,'loco@ejemplo.com'),
# ('Crazy',89,'crazy@ejemplo.com'),
# ('Betobhen',105,'beto@ejemplo.com')
# ]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)
cursor.execute("SELECT*FROM usuarios")

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conexion.commit()
conexion.close()


