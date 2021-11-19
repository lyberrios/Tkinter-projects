"""
Calculadora:
-Debe tener dos campos de texto
-4 botones para las operaciones
-Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

class Calculadora:
    #Constructor

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    #Función para convertir
    def convertirFloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror('Error', 'Introduce bien el número')
        return result

    #Funciones para las operaciones
    def sumar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) + self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) - self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) * self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) / self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo('Resultado', f'El resultado de la operación es: {self.resultado.get()}')
        self.numero1.set('')
        self.numero2.set('')

ventana = Tk()
ventana.title('Ejercicio completo con Tkinter')
ventana.geometry('400x400')
ventana.config(bd=25,)

calculadora = Calculadora(messagebox)

marco = Frame(ventana, width=250, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable= calculadora.numero1, justify='center').pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify='center').pack()

Label(marco, text='').pack()

Button(marco, text='Sumar', command=calculadora.sumar).pack(side='left', fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side='left', fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side='left', fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side='left', fill=X, expand=YES)


ventana.mainloop()