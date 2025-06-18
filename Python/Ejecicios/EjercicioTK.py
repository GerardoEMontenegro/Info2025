import tkinter as tk
import time

ventana = tk.Tk()
ventana.geometry("600x200+1320+0")
ventana.maxsize(600, 200)
ventana.minsize(200, 50)
ventana.configure(bg="Black")
#ventana.attributes("-alpha", 0.09) # Transparencia de la ventana
ventana.wm_attributes(alpha=0.9)
ventana.resizable(True, True)

reloj =tk.Label(ventana, font=("Arial", 50), bg="Black", fg="White")

def actualizar_reloj(): 
    hora_actual = time.strftime("%H:%M:%S")
    reloj.config(text=hora_actual)
    reloj.after(1000, actualizar_reloj)  # Actualiza cada segundo

reloj.pack(expand=True)
actualizar_reloj()
reloj.place(relx=0.5, rely=0.5, anchor="center")

ventana.mainloop()