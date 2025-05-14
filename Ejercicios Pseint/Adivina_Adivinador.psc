Algoritmo Adivina_Adivinador
	Definir intentos, secreto, numelegido como entero
	
	intentos = 0
	secreto = 37
	
	Escribir "Hola! Este juego se llama Adivina Adivinador, en el cual debes elegir un numero del 1 al 100 y tienes 10 intentos."
	Mientras numelegido <> secreto y intentos < 10 Hacer
					
			Escribir "Por favor ingresa un número entro 0 y 100"
			Leer numelegido			
			Si numelegido < 0 o numelegido > 100 Entonces
				intentos = intentos + 1
				Escribir "El número esta fuera de rango. Por favor intente nuevamente. Quedan " (10 - intentos) " intentos"			
			FinSi		
			Si numelegido = 0 o numelegido < secreto Entonces
				intentos = intentos + 1
				Escribir "El número ingresado es Menor al número secreto. Quedan " (10 - intentos) " intentos."
			SiNo
				intentos = intentos + 1
				Escribir "El número ingresado es Mayor al número secreto. Quedan " (10 - intentos) " intentos."			
			FinSi	
		si numelegido = secreto y intentos < 10 Entonces
			escribir "Felicitaciones. El número es correcto!!! Lograste hacerlo en el intento número " intentos " Gracias por Jugar Adivina Adivinador. "				
		FinSi	
		si numelegido <> secreto y intentos >= 10 Entonces
			Escribir "Se acabaron los intentos, mas suerte la próxima!"			
		FinSi		
	FinMientras	
FinAlgoritmo
