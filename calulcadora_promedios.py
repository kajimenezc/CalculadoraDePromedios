

def ingresar_calificaciones():
    """Funcion que solicita el ingreso de materias
        con sus calificaciones"""

    nombres = []
    calificaciones = []
    isAddSubject = True

    while isAddSubject:
        
        while True:
            nombre = input("Ingrese el nombre de la materia: ")
            if len(nombre) == 0:
                print("El nombre de la materia no puede estar vacio")
            elif len(nombre) > 30:
                print("El nombre de la materia no puede tener mas de 30 caracteres")
            else:
                nombres.append(nombre)
                break
        
        while  True:
            try:
                calificacion = float(input("Ingrese una calificacion de 0 a 10: "))
                if calificacion >= 0 and calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe ser mayor a 0 y menor o igual a 10") 
            except ValueError:
                print("Debe ingresar un número válido. Ejemplo: 5.5")
        
        opcion = input("¿Desea agregar otra materia? (si/no): ")

        while True:
            if opcion.lower() != "si" and opcion.lower() != "no":
                opcion = input("Opción inválida. Por favor ingrese 'si' o 'no': ")
            else:
                break

        if opcion.lower() != "si":
            isAddSubject = False   
        
    return nombres, calificaciones



def calcular_promedio(calificaciones):
    """Funcion que realiza el calculo del promedio de las calificaciones"""
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones) 
    return promedio
    

def determinar_estado(calificaciones, umbral, nombres):
    """Funcion que determina las materias aprobadas y reprobadas
        segun un umbral dado"""
    aprobadas = []
    reprobadas = []
    count = 0

    for calificacion in calificaciones:
        
        if calificacion >= umbral:
            aprobadas.append(nombres[count])
        else:
            reprobadas.append(nombres[count])
        count += 1
    
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    """Funcion que encuentra la materia con mejor calificacion y 
        la peor calificacion"""

    if not calificaciones:
        return None, None

    lower_index = min(range(len(calificaciones)), key=lambda i: calificaciones[i])
    upper_index = max(range(len(calificaciones)), key=lambda i: calificaciones[i])

    return lower_index, upper_index
    

def mostrar_resumen(nombres, calificaciones, promedio, aprobadas, reprobadas, lower_index, upper_index):

    print()
    print("------------Materias-------------")
    for nombre, calificacione in zip(nombres, calificaciones):
        print(f"{nombre}, Calificación: {calificacione}")
    print("-----------------------------------")
    print(f"Total Materias: {len(calificaciones)}")
    print("-----------------------------------")
    print()
    print("------------Promedios--------------")
    print()
    print("El promedio de las calificaciones es: ", promedio)
    print()
    print("Materias aprobadas:", ", ".join(aprobadas))
    print("Materias reprobadas:", ", ".join(reprobadas))
    print()
    print(f"Mejor calificacion es {nombres[upper_index]} con: {calificaciones[upper_index]}")
    print(F"Peor calificacion es {nombres[lower_index]} con: {calificaciones[lower_index]}")
    print()
    print("Te agradecemos por usar la calculadora de promedios")
    print()


def main():
    print("Bienvenido a la calculadora de promedios")
    nombres = []
    calificaciones = []

    nombres, calificaciones = ingresar_calificaciones()

    if not calificaciones:
        print("No se ingresaron calificaciones. No se puede calcular el promedio.")
        return

    promedio = calcular_promedio(calificaciones)

    aprobadas, reprobadas = determinar_estado(calificaciones, 5, nombres)

    lower_index, upper_index = encontrar_extremos(calificaciones)

    mostrar_resumen(nombres, calificaciones, promedio, aprobadas, reprobadas, lower_index, upper_index)

if __name__ == "__main__":
    main()


 
    



