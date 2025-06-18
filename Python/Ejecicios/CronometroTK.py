import tkinter as tk

ventana = tk.Tk()

ventana.title("")
ventana.geometry("600x200+1320+0")
ventana.maxsize(600, 200)
ventana.minsize(200, 50)
#ventana.wm_overrideredirect(True)  # Elimina la barra de título de la ventana
ventana.tk_setPalette(background="Black")  # Cambia el color de fondo de la ventana
ventana.wm_attributes("-topmost", True)  # Mantiene la ventana siempre encima de otras
ventana.wm_attributes("-transparentcolor", "Black") # Hace que el color de fondo sea transparente
ventana.resizable(0, 0)
etiqueta = tk.Label(ventana, text="00.00", font=("Arial", 50), fg="White", bg="Black")

etiqueta.pack(pady=20)

def actualizar_cronometro():
    tiempo= float(etiqueta["text"])
    tiempo += 0.01
    etiqueta["text"] = f"{tiempo:.2f}"
    etiqueta.after(1000, actualizar_cronometro)  # Actualiza cada 1000 milisegundos

def detener_cronometro():
    etiqueta.after_cancel(actualizar_cronometro)  # Detiene el cronómetro

boton_iniciar = tk.Button(ventana, text="Iniciar", command=actualizar_cronometro)

boton_detener = tk.Button(ventana, text="Detener", command=detener_cronometro)




boton_iniciar.pack(pady=10, padx=10, side="left")
boton_detener.pack(pady=10, padx=10, side="right")
ventana.mainloop()
# Este código crea un cronómetro simple utilizando Tkinter en Python.