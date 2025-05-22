#Ejercicio 1: Gestión de una lista de compras
lista_compras = []

lista_compras.append("leche")
lista_compras.append("pan")
lista_compras.append("huevos")


print("La lista de compras tiene", (len(lista_compras)), "productos.")

lista_compras.pop(2)

print(lista_compras)


#Ejercicio 2: Contar apariciones
colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
print("El color rojo aparece", (colores.count("rojo")), "veces en la lista.")

colores[2]='amarillo'
print(colores)

#Ejercicio 3: Diccionario de estudiante

estudiante = {
 "nombre": "Ana",
 "edad": 20,
 "materias": ["Matemática", "Historia"]
}

print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])

estudiante["materias"].append("Inglés")


print("El estudiante esta cursando ", len(estudiante["materias"]), "materias.")
print("Materias:", estudiante["materias"])
print("El estudiante tiene un promerio de ", (estudiante.get("promedio", 0)),".")