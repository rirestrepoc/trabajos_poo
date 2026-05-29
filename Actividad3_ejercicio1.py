# Importamos la librería Tkinter para crear la interfaz gráfica
import tkinter as tk

# Creamos la ventana principal
root = tk.Tk()
root.geometry("500x500")  # Definimos el tamaño de la ventana

# -------------------------------
# Clase que calcula el promedio
# -------------------------------
class promedio:
    def __init__(self, n1, n2, n3, n4, n5):
        # Calculamos el promedio de los 5 números
        self.promedio = (n1 + n2 + n3 + n4 + n5) / 5

    # Método que devuelve el texto con el resultado
    def __str__(self):
        return f'El promedio es: {self.promedio}'

# --------------------------------------
# Función que se ejecuta al presionar el botón
# --------------------------------------
def calcular_promedio():
    # Obtenemos los valores escritos en cada Entry y los convertimos a float
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    n3 = float(numero3.get())
    n4 = float(numero4.get())
    n5 = float(numero5.get())

    # Creamos un objeto de la clase promedio con los valores ingresados
    hola = promedio(n1, n2, n3, n4, n5)

    # Creamos un nuevo campo Entry para mostrar el resultado
    resultado = tk.Entry(root)
    resultado.pack()

    # Insertamos el resultado (texto del método __str__) dentro del Entry
    resultado.insert(0,hola)

# --------------------------------------
# Campos de entrada (Entry) para los números
# --------------------------------------
numero1 = tk.Entry(root)
numero1.pack()

numero2 = tk.Entry(root)
numero2.pack()

numero3 = tk.Entry(root)
numero3.pack()

numero4 = tk.Entry(root)
numero4.pack()

numero5 = tk.Entry(root)
numero5.pack()

# --------------------------------------
# Botón que ejecuta la función calcular_promedio()
# --------------------------------------
boton = tk.Button(root, text="Promedio", command=calcular_promedio)
boton.pack()

# Iniciamos el bucle principal de la ventana
root.mainloop()