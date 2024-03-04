import tkinter as tk
from time import strftime

interfaz = tk.Tk()
interfaz.title("Alarma")
interfaz.geometry('500x400')

def reloj():
    formatoReloj = strftime('%H:%M:%S %p')
    label_reloj.config(text=formatoReloj)
    label_reloj.after(1000, reloj)

label_reloj=tk.Label(interfaz, font=('Avance', 24), background='black', foreground='cyan')
label_reloj.pack(anchor='center', pady=30)

reloj()
interfaz.mainloop()