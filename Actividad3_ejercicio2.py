import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

class salario_p:
    def __init__(self,sal,ven):
        if ven>1000000:
            self.salariof=sal+0.1*ven
        else:
            self.salariof=sal
    def __str__(self):
        return f'El salario es: {self.salariof}'

def calcular_salario():
    sal = float(salario.get())
    ven = float(ventas.get())
    hola = salario_p(sal, ven)
    resultado = tk.Label(root, text=hola)
    resultado.pack()

tk.Label(root, text="Salario:").pack()
salario = tk.Entry(root)
salario.pack()

tk.Label(root, text="Ventas:").pack()
ventas = tk.Entry(root)
ventas.pack()

boton = tk.Button(root, text="Mostrar", command=calcular_salario)
boton.pack()
root.mainloop()