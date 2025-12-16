from tkinter import*
from tkinter import filedialog as FileDiaog

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title(" Mi editor")


def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDiaog.askopenfilename(initialdir=".",filetype=(("Ficehro de texto","*.txt"),),title= "Abrir un ficher de texto")

    if ruta !="":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert',contenido)
        fichero.close(ruta+ "   Mi editor")



def guardar():
    global ruta
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end')
        fichero = open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")



def guardar_como():
    global ruta
    mensaje.set("Guardar como fichero")

#Configuraciones de la raiz 

root = Tk()

#Menu superior

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo",command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir")
menubar.add_cascade(menu=filemenu,label="Archivo")


#Caja de texto central 

texto = Text(root)
texto.pack(fill="both",expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consola",12))


#Motor inferiior 

mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje,justify='left')
monitor.pack(side="left")

root.config(menu='left')

root.config(menu=menubar)







root.mainloop()