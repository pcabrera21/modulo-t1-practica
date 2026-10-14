# Gastos Tracker - Sistema de Control Financiero Personal

Aplicación de consola en Python diseñada bajo una arquitectura modular y limpia para la gestión, seguimiento y cálculo consolidado de finanzas personales (ingresos vs. gastos), con persistencia de datos en formato JSON.

---

## Características Principales

- **Gestión de Transacciones:** Registro discriminado entre Ingresos y Gastos con asignación de categorías predefinidas.
- **Validación Robusta:** Control defensivo de errores mediante bloques `try / except` para evitar interrupciones por entradas inválidas o montos negativos.
- **Reporte Consolidado y Balance:** Resumen financiero tabulado que calcula en tiempo real los ingresos acumulados, gastos totales y el balance neto ($Balance = Total_{Ingresos} - Total_{Gastos}$).
- **Persistencia Segura en Disco:** Manejo de archivos JSON mediante *Context Managers* (`with open`), garantizando integridad en la lectura y guardado de datos.
- **Identificación Única (ID):** Generación automática de IDs correlativos para facilitar la eliminación y trazabilidad de registros.

---

## Arquitectura del Proyecto

El código implementa el principio de separación de responsabilidades en tres capas desacopladas:

```text
gastos_tracker/
│
├── app.py                # Interfaz de usuario (CLI) y orquestación del flujo principal
├── logica.py             # Reglas de negocio, validaciones numéricas y operaciones CRUD
├── almacenamiento.py     # Manejo de persistencia, lectura y escritura en archivo JSON
├── gastos.json           # Archivo de base de datos local (generado automáticamente)
└── README.md             # Documentación técnica del proyecto
```

---

## Requisitos Previos

- Python 3.8 o superior instalado en el sistema.
- Terminal compatible (Git Bash, PowerShell o zsh).

---

## Instalación y Ejecución

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd gastos_tracker
   ```

2. Ejecuta el script principal:
   ```bash
   python app.py
   ```

---

## Estructura de Datos (`gastos.json`)

Cada transacción registrada en disco mantiene el siguiente esquema:

```json
[
    {
        "id": 1,
        "descripcion": "Pago Sueldo Mensual",
        "tipo": "Ingreso",
        "monto": 850000.0,
        "categoria": "Sueldo/Venta"
    },
    {
        "id": 2,
        "descripcion": "Supermercado Mensual",
        "tipo": "Gasto",
        "monto": 125000.5,
        "categoria": "Alimentacion"
    }
]
```

---

## Autor

Desarrollado como parte del plan de formación en Fundamentos de Ingeniería de Software e Inteligencia Artificial (Módulo T1).