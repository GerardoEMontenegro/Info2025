import tkinter as tk

class cronometro:
    def __init__(self, ventana):
        self.ventana = ventana
        self.minutos = 0
        self.segundos = 0
        self.activo = False
        self.display = tk.StringVar()
        self.actualizar_cronometro("00:00")
        self.ventana.configure(bg="black")

        self.display_label = tk.Label(ventana, textvariable=self.display, font=("Arial", 50), fg="white", bg="black")
        
