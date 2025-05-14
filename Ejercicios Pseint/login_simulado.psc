Algoritmo login_simulado
    Definir  usuario, contrasenia Como Cadena
    Definir intentos Como Entero
    intentos = 3
    
    Mientras intentos > 0 Hacer
        Escribir 'Ingrese su Usuario:'
        Leer usuario
        Escribir 'Igrese su Contraseña:'
        Leer contrasenia
        
        // usuario -> admin  contraseña -> dificil123 &
        Si usuario = "admin" y contrasenia = "dificil123" Entonces
            Escribir 'Login exitoso. Bienvenido!'
            intentos = 0
        SiNo
            Escribir 'Usuario o contraseña incorrectos!'
            intentos =  intentos - 1
        Fin Si
    Fin Mientras
FinAlgoritmo