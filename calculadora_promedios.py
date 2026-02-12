UMBRAL_APROBACION = 5.0


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
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10 (inclusive).")
            except ValueError:
                print("Debe ingresar un número válido. Ejemplo: 5.5")
        
        opcion = input("¿Desea agregar otra materia? (si/no) [s/n]: ")

        while True:
            opt = opcion.strip().lower()
            if opt in ("si", "s"):
                break
            if opt in ("no", "n"):
                isAddSubject = False
                break
            opcion = input("Opción inválida. Por favor ingrese 'si'/'s' o 'no'/'n': ")
            
        
    return nombres, calificaciones



def calcular_promedio(calificaciones):
    """Funcion que realiza el calculo del promedio de las calificaciones.
    Devuelve None si la lista de calificaciones está vacía."""
    if not calificaciones:
        return None
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    return promedio
    

def determinar_estado(calificaciones, umbral):
    """Funcion que determina los indices de materias aprobadas y reprobadas
        segun un umbral dado. Devuelve dos listas de indices (aprobadas, reprobadas)."""
    aprobadas_idx = []
    reprobadas_idx = []

    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas_idx.append(i)
        else:
            reprobadas_idx.append(i)

    return aprobadas_idx, reprobadas_idx

def encontrar_extremos(calificaciones):
    """Funcion que encuentra la materia con mejor calificacion y 
        la peor calificacion"""

    if not calificaciones:
        return None, None

    lower_index = min(range(len(calificaciones)), key=lambda i: calificaciones[i])
    upper_index = max(range(len(calificaciones)), key=lambda i: calificaciones[i])

    return lower_index, upper_index
    


def mostrar_resumen(nombres, calificaciones, promedio, aprobadas_idx, reprobadas_idx, lower_index, upper_index, umbral):

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
    print(f"Umbral de aprobacion: {umbral}")
    print("El promedio de las calificaciones es:", promedio if promedio is not None else "N/A")
    print()
    aprobadas_nombres = [nombres[i] for i in aprobadas_idx]
    reprobadas_nombres = [nombres[i] for i in reprobadas_idx]
    print("Materias aprobadas:", ", ".join(aprobadas_nombres) if aprobadas_nombres else "Ninguna")
    print("Materias reprobadas:", ", ".join(reprobadas_nombres) if reprobadas_nombres else "Ninguna")
    print()
    if lower_index is None or upper_index is None:
        print("No hay materias para determinar mejor/peor calificación.")
    else:
        print(f"Mejor calificacion es {nombres[upper_index]} con: {calificaciones[upper_index]}")
        print(f"Peor calificacion es {nombres[lower_index]} con: {calificaciones[lower_index]}")
    print()
    print("Te agradecemos por usar la calculadora de promedios")
    print()


def main():
    nombres = []
    calificaciones = []

    nombres, calificaciones = ingresar_calificaciones()

    if not calificaciones:
        print("No se ingresaron calificaciones. No se puede calcular el promedio.")
        return

    promedio = calcular_promedio(calificaciones)

    aprobadas_idx, reprobadas_idx = determinar_estado(calificaciones, UMBRAL_APROBACION)

    lower_index, upper_index = encontrar_extremos(calificaciones)

    mostrar_resumen(nombres, calificaciones, promedio, aprobadas_idx, reprobadas_idx, lower_index, upper_index, UMBRAL_APROBACION)

if __name__ == "__main__":
    print("Bienvenido a la calculadora de promedios")
    main()


 
    



