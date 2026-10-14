from almacenamiento import cargar_transacciones, guardar_transacciones
from logica import registrar_movimiento, mostrar_reporte, eliminar_movimiento, actualizar_movimiento

transacciones = cargar_transacciones()
activo = True

print("=== SISTEMA GASTOS TRACKER - CONTROL FINANCIERO ===")
if transacciones:
    print(f"* Base cargada: {len(transacciones)} transaccion(es) encontradas.")

while activo:
    print("\nMenu Principal:")
    print("1. Registrar movimiento (Ingreso / Gasto)")
    print("2. Ver reporte y balance neto")
    print("3. Modificar movimiento por ID")
    print("4. Eliminar movimiento por ID")
    print("5. Guardar cambios en disco")
    print("6. Salir")

    opcion = input("Selecciona una opcion (1-5): ").strip()

    if opcion == "1":
        registrar_movimiento(transacciones)

    elif opcion == "2":
        mostrar_reporte(transacciones)

    elif opcion == "3":
        actualizar_movimiento(transacciones)

    elif opcion == "4":
        eliminar_movimiento(transacciones)

    elif opcion == "5":
        guardar_transacciones(transacciones)

    elif opcion == "6":
        guardar_transacciones(transacciones)
        print("> Cerrando el sistema de finanzas. Hasta pronto!")
        activo = False

    else:
        print("! Opcion no valida. Ingresa un numero del 1 al 6.")