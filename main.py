import tkinter as tk
import random

ventana = tk.Tk()
ventana.title("Matriz Cuadrada")
ventana.iconbitmap('ico/logo21.ico')
ventana.geometry("500x500")
ventana.resizable(0,0)


# Función para crear la matriz cuadrada
def crear_matriz():
    num = int(num_filas_columnas.get())
    
    
    # widget canvas
    canvas = tk.Canvas(ventana, width=400, height=400)
    canvas.place(y=5, x=50)
    
    # rectángulos
    x1 = 0
    y1 = 0
    x2 = 400/num
    y2 = 400/num
    color = "white"
    
    # números aleatorios
    num_aleatorios = []
    for i in range(num**2):
        num_aleatorios.append(random.randint(1,100))
    
    # rectángulos con los números aleatorios
    contador = 0
    for i in range(num):
        for j in range(num):
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            canvas.create_text(x1+20, y1+20, anchor="nw", text=str(num_aleatorios[contador]))
            x1 += 400/num
            x2 += 400/num
            contador += 1
        x1 = 0
        y1 += 400/num
        x2 = 400/num
        y2 += 400/num
    
    # Función para buscar el número
    def buscar_numero():
        contador = 0
        numero_buscar = int(numero_entrada.get())
        x1 = 0
        y1 = 0
        x2 = 400/num
        y2 = 400/num
        for i in range(num):
            for j in range(num):
                if num_aleatorios[contador] == numero_buscar:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
                    canvas.create_text(x1+20, y1+20, anchor="nw", text=str(num_aleatorios[contador]))
                x1 += 400/num
                x2 += 400/num
                contador += 1
            x1 = 0
            y1 += 400/num
            x2 = 400/num
            y2 += 400/num
    
    # label
    tex2 = tk.Label(text="Buscar:")
    tex2.place(x=245, y=417)
    # widget entry para ingresar el número
    numero_entrada = tk.Entry(ventana,  font="Rubik 16")
    numero_entrada.place(x=290, y=415, width=140, height=30)
    
    # botón para buscar el número
    boton_buscar = tk.Button(ventana, text="Buscar Número", command=buscar_numero)
    boton_buscar.place(x=290, y=455, width=140, height=30)
    


# label
tex1 = tk.Label(text="Tamaño:")
tex1.place(x=35, y=417)
    
# widget entry para ingresar el número de filas y columnas
num_filas_columnas = tk.Entry(ventana, font="Rubik 16")
num_filas_columnas.place(x=90, y=415, width=140, height=30)

# botón para crear la matriz
boton_crear_matriz = tk.Button(ventana, text="Crear Matriz", command=crear_matriz)
boton_crear_matriz.place(x=90, y=455, width=140, height=30)

ventana.mainloop()