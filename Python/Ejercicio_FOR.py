numeros = []
par = 0
impar = 0

for i in range(10):
    num = int(input("Introduce un numero: "))
    numeros.append(num)

for n in numeros:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
  
print("la lista de numeros es:" , numeros)
print("La cantidad de numeros pares es: ", par)
print("La cantidad de numeros impares es: ", impar)