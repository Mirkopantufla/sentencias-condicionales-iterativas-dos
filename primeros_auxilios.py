# Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
# entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
# en tiempo real.

# Se añade excepcion para cada caso, asi se evita 
# Inicializo en falso, por que la ambulancia no esta al iniciar el programa
ambulancia = False

# Pregunto si tiene respuesta a estimulos
respuestaEstimulos = input("¿Responde a estimulos? (si o no): ").lower() # Se añade funcion para pasar todo a lower, y evitar problemas por Mayusculas

if(respuestaEstimulos == "si"):
    print("Valorar la necesidad de llevarlo al hospital más cercano")
elif(respuestaEstimulos == "no"):
    print("Abrir la via aérea")
    # Pregunto si respira
    respuestaRespira = input("¿Respira?  (si o no): ").lower()

    if(respuestaRespira == "si"):
        print("Permitirle posición de suficiente respiración")
    elif(respuestaRespira == "no"):
        print("Administrar 5 ventilaciones y llamar a Ambulancia")
        while(ambulancia == False):
            # Pregunto si tiene signosDeVida
            signosDeVida = input("¿Signos de Vida? (si o no): ").lower()

            if(signosDeVida == "si"):
                print("Reevaluar a la espera de la ambulancia")
            elif(signosDeVida == "no"):
                print("Administrar compresiones Torácicas hasta que llegue la ambulancia")
            else:
                print("La respuesta debe ser si o no")

            # Pregunto si llego la ambulancia, y cambio el estado de la ambulancia para salir del while
            arriboAmbulancia = input("¿Llego la ambulancia? (si o no): ").lower()
            if(arriboAmbulancia == "si"):
                ambulancia = True
            elif(arriboAmbulancia == "no"):
                ambulancia = False
            else:
                print("La respuesta debe ser si o no")

else:
    print("La respuesta debe ser si o no")






print("Fin")