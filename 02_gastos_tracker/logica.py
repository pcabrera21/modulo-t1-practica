CATEGORIAS_VALIDAS = ["Alimentacion", "Transporte", "Servicios", "Salud", "Otros"]

def pedir_monto():
    while True:
        try:
            monto = float(input("Monto CLP($): "))
            if monto <= 0:
                print("! Error: el onto debe ser mayor a 0.")
                continue
            return round(monto, 2)
        except ValueError:
            print("! Error: Ingrese un numero valido (e: 1500 ó 2500.50)")

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