from funciones import *

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            asignar_sueldos_aleatorios()
        elif opcion == "2":
            clasificar_sueldos()
            pass
        elif opcion == "3":
            ver_estadisticas_sueldos()
            pass
        elif opcion == "4":
            reporte_sueldos()
            print(f"La planilla ha sido guardada en '{nombre_archivo}'")
            pass
        elif opcion == "5":
            print("Haz salido del programa.")          
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-5).")

if __name__ == "__main__":
     main()
