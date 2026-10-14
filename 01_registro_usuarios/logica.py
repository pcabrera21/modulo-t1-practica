def clasificar_edad(edad):
    #clasificacion logica
    if edad < 18:
        categoria = "Menor de edad."
        return categoria
    elif edad < 65:
        categoria = "Adulto activo."
        return categoria
    else:
        categoria = "Adulto mayor."
        return categoria

def pedir_edad():
    #Validacion edad con try / except
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0 or edad > 120:
                print("!Error: la edad debe estar entre 0 y 120 años.")
                continue #vuleve ciclo while si esta fuera de rango
            #break #sale del ciclo o bucle sólo si ingresa el dato de forma correcta o en rango validado
            return edad
        except ValueError:
            print("!Error: Debes ingresar un numero entero válido (sin letras) ni simbolos") #Vuelve al bucle si ingresa un valor distinto a un numero entero

def eliminar_usuario(lista_usuarios):
    if not lista_usuarios:
        print("> No hay registros disponibles para eliminar.")
        return

    print("\n-- SELECCIONA EL REGISTRO A ELIMINAR --")
    for indice, u in enumerate(lista_usuarios, start=1):
        print(f"{indice}. {u['nombre']} | {u['edad']} años | {u['categoria']}")

    while True:
        try:
            opcion = int(input("\n Ingrese el numero del registro a eliminar (preione 0 para cancelar): "))
            if opcion == 0:
                print("> Operacion cancelada.")
                break

            #En python los indices van de 0 a len-1, por eso restamos -1
            if 1 <= opcion <= len(lista_usuarios):
                eliminado = lista_usuarios.pop(opcion-1)
                print(f"> Registro de '{eliminado['nombre']}' eliminado con exito.")
                break
            else:
                print(f"! Error: Debes ingresar un numero entre 1 y {len(lista_usuarios)}.")
        except ValueError:
            print("! Error: Debes ingresar un numero valido.")


def editar_usuario(lista_usuarios):
    if not lista_usuarios:
        print("> No hay registros disponibles para editar.")
        return

    print("\n--- SELECCIONA EL REGISTRO A EDITAR")
    for indice, u in enumerate(lista_usuarios, start=1):
        print(f"{indice}, {u['nombre']} | {u['edad']} años | {u['categoria']}")

    while True:
        try:
            opcion = int(input("\n Ingrese el numero del registro a editar (0 para cancelar): "))
            if opcion == 0:
                print("> Operacion Cancelada.")
                break

            if 1 <= opcion <=len(lista_usuarios):
                usuario_actual = lista_usuarios[opcion - 1]
                print(f"\nEditando a: {usuario_actual['nombre']} ({usuario_actual['edad']} años)")

                #Editar nombre (presionar enter mantiene el actual)
                nuevo_nombre = input(f"Nuevo nombre (Enter para mantener {usuario_actual['nombre']}): ")
                if nuevo_nombre:
                    usuario_actual["nombre"] = nuevo_nombre

                #Preguntar si desea cambiar la edad
                cambiar_edad = input("Deseasmodificar la edad? (s/n)").strip().lower()
                if cambiar_edad == "s":
                    nueva_edad = pedir_edad()
                    usuario_actual["edad"] = nueva_edad
                    usuario_actual["categoria"] = clasificar_edad(nueva_edad)

                print(f">> Registro actualizado con exito: {usuario_actual['nombre']} | {usuario_actual['edad']} | {usuario_actual['categoria']}")
                break
            else:
                print(f"! Error: debes ingresar un numero entre 1 y {len(lista_usuarios)}")
        except ValueError:
            print("! Error: debes ingresar un numero valido.")

