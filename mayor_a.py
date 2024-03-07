import sys
# Actividad 1 - Filtrado compacto
# Se solicita devolver un informe resumido que exponga los meses que superan un cierto
# umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor asociado
# siempre y cuando superen el umbral especificado. 

ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

filteredMonths = {}

# Por cada item de venta, se compara el valor de cada mes y se crea una diccionario aparte para almacenar la nueva informacion
for key, value in ventas.items():
    # Si el valor es mayor a lo comparado, se guarda en la nueva lista
    if(value > int(sys.argv[1])):
        filteredMonths[key] = value


print(filteredMonths)