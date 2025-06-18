import random
from mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 0
        self.hambre = 0
        self.imagen = imagen.inicio
        self.imagen = imagen.triste
        self.imagen = imagen.muerto
        self.imagen = imagen.disgustado
        self.imagen = imagen.feliz


    def alimentar(self):
        self.felicidad -= random.randint(5, 10)
        if self.felicidad < 0:
            self.felicidad = 0
        if self.hambre == 0:
            print(self.imagen.disgustado)
            print(f"{self.nombre} esta lleno, ya no puede comer mas.")
        else:
            self.hambre -= random.randint(10, 15)
            if self.hambre < 0:
                self.hambre = 0
            print(self.imagen.feliz)
            print(f"{self.nombre} ha sido alimentado.😘")


    def jugar(self):
        pass

    def estado_animo(self):
        pass

    def presentacion(self): 
        print(
f"\n╔════════════════════════════════════╗\n║ Te presento a tu mascota! ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}"
)
    def despedida(self):  # opcional
        print(
f"\n╔════════════════════════════════════╗\n║ Nos vemos! ║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║ Jueguemos otro día! ║\n╚════════════════════════════════════╝\n"
)


# Crear una instancia de MascotaVirtual

# Interactuar con la mascota virtual
# alimenta, juega y muestra su estado de animo
# repite esta accion al menos 8 veces

# Esto lo vamos a utilizar más adelante 😉
interfaz_inicio = "\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n"
interfaz_juego = "\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar                      ║\n║ 2 - Jugar                          ║\n║ 3 - Mostrar informacion            ║\n║ 4 - Salir                          ║\n║                                    ║\n╚════════════════════════════════════╝\n"



nombre = input("Elige un nombre para tu mascota: ")

mascota = MascotaVirtual(nombre)
mascota.presentacion()
while True:
    print(interfaz_juego)
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == 1:
        mascota.alimentar()
    elif opcion == 2:
        mascota.jugar()
    elif opcion == 3:
        mascota.estado_animo()
    elif opcion == 4:
        mascota.despedida()
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")