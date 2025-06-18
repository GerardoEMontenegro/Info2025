# [Mascota Virtual:](/Mascota/)

Crea una clase llamada **_MascotaVirtual_** que simule el comportamiento de una mascota virtual. La mascota tendrá un nombre, un nivel de hambre y un nivel de felicidad.

`Para este ejercicio necesitas importar el modulo random y usar la funcion randint(min, max) que devuelve un entero de entre min y max.
Tambien tendras a disposicion el modulo mascota que contiene un objeto 'imagen' con los atributos: inicio, triste, muerto, disgustado y feliz. prueba imprimirlos para ver que sucede.`

La clase **_MascotaVirtual_** debe tener los siguientes métodos:

\_\_init\_\_(self, nombre):

- Constructor que recibe el nombre de la mascota
  y establece su nivel de hambre y felicidad en 0.

alimentar(self):

- Este método simula alimentar a la mascota. Reduce el nivel de hambre de la mascota en un valor aleatorio entre 10 y 15.
  - Si el nivel de hambre al ejecutar el metodo es 0 muestra el mensaje de que la mascota esta llena y no puede comer mas.
  - Si el nivel de hambre es menor a 0, se establece en 0.
  - Muestra un mensaje de que la mascota fue alimentada.
  - Cada vez que se ejecute el metodo la felicidad de la mascota debe disminuir un valor aleatorio entre 5 y 10. Si el nivel de felicidad es menor a 0, se establece en 0.

jugar(self):

- Este método simula jugar con la mascota.
  - Aumenta el nivel de felicidad de la mascota en un valor aleatorio entre 10 y 25.
  - Si el nivel de felicidad es mayor a 100, se establece en 100.
  - Este método también aumenta el hambre de la mascota entre 10 a 15, si el hambre es mayor a 100 entonces se establece en 100, y si el hambre de la mascota es superior a 70 entonces este metodo jugar() ya no tendra ningun efecto.
  - El metodo muestra un mensaje "se divierte" o "tiene mucha hambre y no puede jugar"

mostrar_estado(self):

- Este método muestra en pantalla el nombre de la mascota, y su estado de ánimo.

  - Si el nivel de hambre es mayor o igual a 70 y el nivel de felicidad es menor o igual a 50, el estado es "muy hambrienta y muy triste".
  - Si el nivel de hambre es mayor o igual a 70, el estado es "muy hambrienta".
  - Si el nivel de felicidad es menor o igual a 50, muestra un estado de animo "muy triste".
  - Si ninguna de estas tres condiciones se cumple, el estado de la mascota es "contenta y satisfecha".

---

Crea una instancia de la clase **_MascotaVirtual_** con el
nombre "Firulais" y realiza las siguientes acciones:

1. Alimenta a la mascota.
2. Juega con la mascota.
3. Muestra el estado de ánimo de la mascota.
4. Repite estas acciones al menos 8 veces para simular la interacción continua con la mascota.

¡Diviértete interactuando con tu mascota virtual y asegúrate de adaptar el nombre y los mensajes a tu gusto!

Opcionales:

- puedes agregar las "imagenes" facilitadas para ilustrar el estado y acciones de la mascota
- puedes agregar un metodo de presentacion y despedida
- si te animas podes agregar una interfaz para poder jugar con la mascota.

[Volver al inicio](/readme.md)
