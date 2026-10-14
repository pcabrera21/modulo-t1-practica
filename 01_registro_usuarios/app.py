from logica import clasificar_edad, pedir_edad, eliminar_usuario, editar_usuario
from almacenamiento import guardar_datos, cargar_datos

#carga inicial automatica
usuarios = cargar_datos()
activo = True

print("=== SISTEMA DE REGISTRO - MODULO T1 ===")

if usuarios:
    print(f"* Se cargaron {len(usuarios)} usuario(s) existentes.")

while activo:
    print("\nOpciones disponibles: ")
    print("1. Registrar nuevo usuario")
    print("2. Mostrar reporte consolidado")
    print("3. Editar usuario")
    print("4. Eliminar usuario")
    print("5. Guardar cambios en disco")
    print("6. Salir")

    opcion = input("Selecciona una opcion (1-4): ")

    if opcion == "1":
        nombre = input("Nombre: ")

        #Llamadas limpias a funciones
        edad = pedir_edad()
        categoria = clasificar_edad(edad)

        # Almacenar como diccionario dentro de la lista
        usuarios.append({
            "nombre": nombre,
            "edad": edad,
            "categoria": categoria
        })
        print(f"> Registro exitoso: {nombre} agregado.")

    elif opcion == "2":
        if len(usuarios) == 0:
            print("> No hay usuarios registrados aún.")
        else:
            print("\n--- REPORTE CONSOLIDADO ---")
            for indice, u in enumerate(usuarios, start=1): #explicarme
                print(f"{indice}. {u['nombre']} | {u['edad']} años | {u['categoria']}")
            print(f"Total registros: {len(usuarios)}")
            print("----------------------------------")

    elif opcion == "3":
        editar_usuario(usuarios)
    
    elif opcion =="4":
        eliminar_usuario(usuarios)

    elif opcion == "5":
        guardar_datos(usuarios)

    elif opcion == "6":
        print("> Cerrando el sistema, Hasta Pronto!")
        activo = False

    else:
        print("! Opcion no valida. Ingrese 1. 2, 3, 4, 5 ó 6... ")