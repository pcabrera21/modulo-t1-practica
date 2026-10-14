CATEGORIAS_VALIDAS = ["Alimentacion", "Transporte", "Servicios", "Salud", "Otros"]

def pedir_monto():
    while True:
        try:
            monto = float(input("Monto CLP($): "))
            if monto <= 0:
                print("! Error: el monto debe ser mayor a 0.")
                continue
            return round(monto, 2)
        except ValueError:
            print("! Error: Ingrese un numero valido (ej: 1500 ó 2500.50)")

def pedir_tipo():
    while True:
        print("Tipo de movimiento: [1] Ingreso | [2] Gasto")
        opcion = input("Selecciona [1] ó [2]: ").strip()
        if opcion == "1":
            return "Ingreso"
        elif opcion == "2":
            return "Gasto"
        print("! Error: Opcion no valida. Ingrese [1] ó [2] ")

def pedir_categoria(tipo):
    if tipo == "Ingreso":
        return "Sueldo/Venta"

    print("\nCategorias disponibles: ")
    for idx, cat in enumerate(CATEGORIAS_VALIDAS, start=1):
        print(f"{idx}. {cat}")

    while True:
        try:
            opcion = int(input("Selecciona categoria (1-5): "))
            if 1<= opcion <= len(CATEGORIAS_VALIDAS):
                return CATEGORIAS_VALIDAS[opcion-1]
            print(f"! Error: Ingresa un numero entre 1 y {len(CATEGORIAS_VALIDAS)}")
        except ValueError:
            print("! Error: Ingresa un numero entero valido.")

def registrar_movimiento(lista):
    descripcion = input("\nDescripcion del movimiento: ").strip()
    while not descripcion:
        print("! Error: La descripcion no puede estar vacia.")
        descripcion = input("Descripcion: ").strip()

    tipo = pedir_tipo()
    monto = pedir_monto()
    categoria = pedir_categoria(tipo)

    nuevo_id = 1 if not lista else max(item["id"] for item in lista) + 1
    
    movimiento = {
        "id": nuevo_id,
        "descripcion": descripcion,
        "tipo": tipo,
        "monto": monto,
        "categoria": categoria
    }

    lista.append(movimiento)
    print(f"> {tipo} registrado con exito [ID: {nuevo_id}]: ${monto:,.2f}")


def mostrar_reporte(lista):
    if not lista:
        print("> No hay transacciones registradas.")
        return

    total_ingresos = 0.0
    total_gastos = 0.0

    print("\n============ DETALLE DE MOVIMIENTOS ============")
    for item in lista:
        signo = "+" if item["tipo"] == "Ingreso" else "-" 
        print(f"[{item['id']}] {item['tipo']:<7} | {item['categoria']:<12} | {item['descripcion']:<20} | {signo}${item['monto']:>10,.2f}")

        if item["tipo"] == "Ingreso":
            total_ingresos += item["monto"]
        else:
            total_gastos += item["monto"]

    balance = total_ingresos - total_gastos

    print("--------------------------------------------------------")
    print(f"TOTAL INGRESOS : ${total_ingresos:>12,.2f}")
    print(f"TOTAL GASTOS   : ${total_gastos:>12,.2f}")
    print(f"BALANCE NETO   : ${balance:>12,.2f}")
    print("========================================================")


def eliminar_movimiento(lista):
    if not lista:
        print("> No hay transacciones para eliminar.")
        return

    mostrar_reporte(lista)

    while True:
        try:
            id_eliminar = int(input("\nIngresa el ID del movimiento a eliminar (0 para cancelar): "))
            if id_eliminar == 0:
                print("> Operacion cancelada.")
                break

            encontrado = None
            for idx, item in enumerate(lista):
                if item["id"] == id_eliminar:
                    encontrado = idx
                    break

            if encontrado is not None:
                eliminado = lista.pop(encontrado)
                print(f"> Movimiento [ID: {eliminado['id']}] '{eliminado['descripcion']}' eliminado con éxito")
                break
            else:
                print(f"> Error: No existe un movimiento con ID {id_eliminar}.")

        except ValueError:
            print("! Error: Ingrese un numero valido.")


def actualizar_movimiento(lista):
    if not lista:
        print("> No hay transacciones para modificar.")
        return

    mostrar_reporte(lista)

    # 1. Fase de selección de ID
    movimiento_seleccionado = None
    while True:
        try:
            id_input = input("\nIngresa el ID del movimiento a modificar (0 para cancelar): ").strip()
            id_buscado = int(id_input)
            
            if id_buscado == 0:
                print("> Operacion cancelada.")
                return

            for item in lista:
                if item["id"] == id_buscado:
                    movimiento_seleccionado = item
                    break

            if movimiento_seleccionado is not None:
                break
            else:
                print(f"! Error: No existe un movimiento con ID {id_buscado}. Intenta de nuevo.")

        except ValueError:
            print("! Error: El ID debe ser un numero entero valido.")

    # 2. Fase de edición (ya tenemos el elemento garantizado)
    print(f"\n--- MODIFICANDO REGISTRO [ID {movimiento_seleccionado['id']}] ---")
    print(f"Actual: {movimiento_seleccionado['descripcion']} | ${movimiento_seleccionado['monto']:,.2f} | {movimiento_seleccionado['tipo']} ({movimiento_seleccionado['categoria']})")
    print("1. Modificar descripcion")
    print("2. Modificar monto")
    print("3. Modificar tipo y categoria")
    print("4. Modificar todo el registro")
    print("5. Cancelar")

    opcion_edicion = input("Selecciona que deseas cambiar (1-5): ").strip()

    if opcion_edicion == "1":
        nueva_desc = input("Nueva descripcion: ").strip()
        while not nueva_desc:
            print("! Error: La descripcion no puede estar vacia.")
            nueva_desc = input("Nueva descripcion: ").strip()
        movimiento_seleccionado["descripcion"] = nueva_desc
        print("> Descripcion actualizada con exito.")

    elif opcion_edicion == "2":
        nuevo_monto = pedir_monto()
        movimiento_seleccionado["monto"] = nuevo_monto
        print(f"> Monto actualizado con exito a: ${nuevo_monto:,.2f}")

    elif opcion_edicion == "3":
        nuevo_tipo = pedir_tipo()
        nueva_cat = pedir_categoria(nuevo_tipo)
        movimiento_seleccionado["tipo"] = nuevo_tipo
        movimiento_seleccionado["categoria"] = nueva_cat
        print(f"> Tipo actualizado a {nuevo_tipo} ({nueva_cat}).")

    elif opcion_edicion == "4":
        nueva_desc = input("Nueva descripcion: ").strip()
        while not nueva_desc:
            print("! Error: La descripcion no puede estar vacia.")
            nueva_desc = input("Nueva descripcion: ").strip()
        nuevo_tipo = pedir_tipo()
        nuevo_monto = pedir_monto()
        nueva_cat = pedir_categoria(nuevo_tipo)

        movimiento_seleccionado["descripcion"] = nueva_desc
        movimiento_seleccionado["tipo"] = nuevo_tipo
        movimiento_seleccionado["monto"] = nuevo_monto
        movimiento_seleccionado["categoria"] = nueva_cat
        print("> Registro completo actualizado con exito.")

    elif opcion_edicion == "5":
        print("> Sin modificaciones realizadas.")

    else:
        print("! Opcion no valida. Regresando al menu principal.")



