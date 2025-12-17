import sqlite3

#Menu de restaurate con conexion a base de datos SQLlite 

def crear_db():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla categorias ya existe")
    else:
        print("La tabla de categorias se ha creado correctamente")

    try:
        cursor.execute('''CREATE TABLE plato(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre VARCHAR(100) UNIQUE NOT NULL,
                   categoria_id INTEGER NOT NULL,
                   FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla platos ya existe")
    else:
        print("La tabla de platos se ha creado correctamente")

    conexion.commit()
    conexion.close()


def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoria?\n> ")
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria (nombre) VALUES (?)", (categoria,))
    except sqlite3.IntegrityError:
        print(f"La categoria '{categoria}' ya existe.")
    else:
        print(f"Categoria '{categoria}' creada correctamente.")

    conexion.commit()
    conexion.close()


def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria para añadir un plato: ")

    for categoria in categorias:
        print(f" [{categoria[0]}] {categoria[1]}")

    categoria_usuario = int(input("> "))
    plato = input("¿Nombre del nuevo plato?\n> ")

    try:
        cursor.execute("INSERT INTO plato (nombre, categoria_id) VALUES (?, ?)", (plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print(f"El plato '{plato}' ya existe.")
    else:
        print(f"Plato '{plato}' creado correctamente.")

    conexion.commit()
    conexion.close()


def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id=?", (categoria[0],)).fetchall()
        for plato in platos:
            print(f"\t{plato[1]}")

    conexion.close()


# Crear base de datos
crear_db()

# Menú de opciones
while True:
    print("\nBienvenido al gestor del restaurante")
    opcion = input("\nIntroduce una opción: \n[1] Agregar categoria\n[2] Agregar plato\n[3] Mostrar menú\n[4] Salir\n> ")

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        print("Nos vemos")
        break
    else:
        print("Opción incorrecta")
   