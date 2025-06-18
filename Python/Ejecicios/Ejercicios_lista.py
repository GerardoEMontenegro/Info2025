print("--- Tuplas ---")

frutas = ("manzana", "banana", "naranja")
verduras = ("lechuga", "cebolla", "zanahoria")


print("Elemento del indice 0 es:", frutas[0])
print("Elemento del indice 2 es:", frutas[2])

#Longitud de la tupla
print("La longitud de la tupla frutas es:", len(frutas))

print("La fruta manzana esta en la posicion:", frutas.index("manzana"))
print(f"La fruta Manzana aparece {frutas.count("manzana")} veces en la tupla")


uno, dos, tres = frutas


#concatenar tuplas

tupla3 = frutas + verduras

print(tupla3)