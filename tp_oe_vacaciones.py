empleados = [
    {"nombre": "Ana", "dias": 15},
    {"nombre": "Juan", "dias": 8},
    {"nombre": "Luis", "dias": 10}
]


def buscar_empleado(nombre):
    for emp in empleados:
        if emp["nombre"].lower() == nombre.lower():
            return emp
    return None


def solicitar_vacaciones():
    print("\n--- SOLICITAR VACACIONES ---")

    nombre = input("Nombre del empleado: ").strip()

    if nombre == "":
        print(" Error: nombre vacío")
        return

    empleado = buscar_empleado(nombre)

    if not empleado:
        print(" Empleado no encontrado")
        return

    try:
        dias = int(input("Días solicitados: "))

        if dias <= 0:
            print("Error: días inválidos")
            return

        if dias > empleado["dias"]:
            print(" No tiene suficientes días disponibles")
            return

        empleado["dias"] -= dias
        print(" Vacaciones aprobadas")
        print("Días restantes:", empleado["dias"])

    except ValueError:
        print(" Error: debes ingresar un número")


def ver_empleados():
    print("\n--- EMPLEADOS ---")
    for emp in empleados:
        print(f"{emp['nombre']} - {emp['dias']} días")


def main():
    while True:
        print("\n===== SISTEMA DE VACACIONES =====")
        print("1. Solicitar vacaciones")
        print("2. Ver empleados")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            solicitar_vacaciones()
        elif opcion == "2":
            ver_empleados()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("1 Opción inválida")


# INICIO DEL PROGRAMAS
main()
