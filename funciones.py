import random
import math
import csv
import statistics
nombre_archivo = 'planilla_de_sueldos.csv()'

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", 
                "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", 
                "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

def generar_sueldos_aleatorios():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos
sueldos = generar_sueldos_aleatorios()
print(sueldos)

def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas de sueldos")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def asignar_sueldos_aleatorios():
    sueldos = generar_sueldos_aleatorios()
    print("\nSueldos asignados aleatoriamente:")
    for i, trabajador in enumerate(trabajadores):
        print(f"{trabajador}: ${sueldos[i]}")

def clasificar_sueldos():
    menores_800000 = []
    entre_800000_y_2000000 = []
    superiores_2000000 = []

    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            menores_800000.append((trabajadores[i], sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800000_y_2000000.append((trabajadores[i], sueldo))
        else:
            superiores_2000000.append((trabajadores[i], sueldo))
    total_sueldos = sum(sueldos)

    print("\nSueldos menores a $800.000")
    print(f"TOTAL: {len(menores_800000)}")
    for trabajador, sueldo in menores_800000:
        print(f"Nombre empleado: {trabajador}, Sueldo: ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(entre_800000_y_2000000)}")
    for trabajador, sueldo in entre_800000_y_2000000:
        print(f"Nombre empleado: {trabajador}, Sueldo: ${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(superiores_2000000)}")
    for trabajador, sueldo in superiores_2000000:
        print(f"Nombre empleado: {trabajador}, Sueldo: ${sueldo}")

    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

def ver_estadisticas_sueldos():
    promedio = statistics.mean(sueldos)
    mediana = statistics.median(sueldos)
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    media_geometrica = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))

    print("\nEstadísticas de sueldos:")
    print(f"Promedio: ${promedio:.2f}")
    print(f"Mediana: ${mediana:.2f}")
    print(f"Sueldo máximo: ${sueldo_max}")
    print(f"Sueldo mínimo: ${sueldo_min}")

def reporte_sueldos(): 
    print("\nReporte de sueldos:")
    print(f"{'Nombre empleado':<20}{'Sueldo Base':<15}{'Descuento Salud':<20}{'Descuento AFP':<15}{'Sueldo Líquido':<15}")
    for i, trabajador in enumerate(trabajadores):
        sueldo_base = sueldos[i]
        descuento_salud = sueldo_base * 0.07
        descuento_afp = sueldo_base * 0.12
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        print(f"{trabajador:<20}${sueldo_base:<14.2f}${descuento_salud:<19.2f}${descuento_afp:<14.2f}${sueldo_liquido:<14.2f}")
    
    nombre_archivo = 'planilla_de_sueldos.csv.'

    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        
        for i, trabajador in enumerate(trabajadores):
            sueldo_base = sueldos[i]
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
            writer.writerow([trabajador, f'${sueldo_base:.2f}', f'${descuento_salud:.2f}', f'${descuento_afp:.2f}', f'${sueldo_liquido:.2f}'])

