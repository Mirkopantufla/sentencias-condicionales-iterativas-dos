from string import ascii_lowercase as letras

password = input("Ingrese su contraseña (no considera la ñ): ").lower() # Se añade funcion para pasar todo a lower, y evitar problemas por Mayusculas
contador = 0 # Inicializo el contador en 0

for char in password:
    for letra in letras:
        # Suma uno al contador, cada vez que entre al loop para comparar
        contador += 1
        if(char == letra):
            # En el caso de encontrar la letra, sale del loop actual para no seguir contando
            break
    
print(f"La contraseña fue forzada en {contador} intentos") # Imprimo el valor