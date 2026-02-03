

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
                calificacion = float(input("Ingrese una calificacion de 1 a 10: "))
                if calificacion >= 1 and calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe ser mayor a 1 y menor o igual a 10") 
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
    print("El promedio de las calificaciones es: ", promedio)
    

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
    
    print("Materias aprobadas:", ", ".join(aprobadas))
    print("Materias reprobadas:", ", ".join(reprobadas))
    
    return aprobadas, reprobadas

def encontrar_extremos(nombres, calificaciones):
    """Funcion que encuentra la materia con mejor calificacion y 
        la peor calificacion"""
    count = 0
    lower_index = 0
    lower_value = 10
    lower_name = ""
    upper_index = 0
    upper_value = 1
    upper_name = ""

    for calificacion in calificaciones:
        
        if calificacion <= lower_value:
            lower_index = count
            lower_value = calificacion
            lower_name = nombres[count]

        if calificacion > upper_value:
            upper_index = count
            upper_value = calificacion
            upper_name = nombres[count]

        count += 1

    print(f"Mejor calificacion es {(upper_name)} con: ", upper_value)
    print(F"Peor calificacion es {(lower_name)} con: ", lower_value)
    
    return lower_index, upper_index
    


def main():
    print("Bienvenido a la calculadora de promedios")
    nombres = []
    calificaciones = []

    nombres, calificaciones = ingresar_calificaciones()

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
    calcular_promedio(calificaciones)
    print()
    determinar_estado(calificaciones, 5, nombres)
    print()
    encontrar_extremos(nombres, calificaciones)
    print()
    print()
    print("Te agradecemos por usar la calculadora de promedios")

if __name__ == "__main__":
    main()


 
    



