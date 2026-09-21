import numpy as np
import csv

# Lista de los departamentos
departamentos = [
    "Lima",
    "Arequipa",
    "Cusco",
    "Piura",
    "La Libertad"
]

# Semilla
semilla = 72641

# Generador de números aleatorios
rng = np.random.default_rng(semilla)

# Lista que contiene la población
poblacion = rng.integers(500000, 11000000, size=5)

# Lista que contiene el ingreso promedio mensual
ingresos_promedio = rng.integers(1600, 3501, size=5)

# Lista que contiene el número de hogares
numero_hogares = rng.integers(150000, 3000000, size=5)

# Lista que contiene la actividad económica
actividad_economica_predominante = [
    "Servicios",
    "Comercio",
    "Turismo",
    "Agricultura",
    "Manufactura"
]

# Tupla que contiene los períodos
periodo = ("2020", "2024")

# Diccionario
informacion_region = {
    "departamentos": departamentos,
    "poblacion": poblacion.tolist(),
    "ingresos_promedio": ingresos_promedio.tolist(),
    "numero_hogares": numero_hogares.tolist(),
    "actividad_economica_predominante": actividad_economica_predominante
}

# Segundo elemento de la lista departamentos
print("Segundo departamento:", departamentos[1])

# Primer y último elemento de la tupla
print("Primer período:", periodo[0])
print("Último período:", periodo[-1])

# Valores de ingreso_promedio del diccionario
print("Ingresos promedio:", informacion_region["ingresos_promedio"])

# Calcula la diferencia entre el primer y último elemento de ingresos_promedio
diferencia = ingresos_promedio[0] - ingresos_promedio[-1]

# Presenta la diferencia calculada
print("Diferencia entre el primer y último ingreso:", diferencia)

# Crea una lista de diccionarios para almacenar los datos que serán exportados
datos = []

# Recorre los cinco departamentos para organizar la información
for i in range(5):
    datos.append({
        "Departamento": departamentos[i],
        "Poblacion": poblacion[i],
        "Ingreso": ingresos_promedio[i],
        "Numero_hogares": numero_hogares[i],
        "Actividad_principal": actividad_economica_predominante[i]
    })

# Nombre del CSV
nombre_archivo = "data/datos_economicos.csv"

# Crea y escribe el archivo CSV
with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:

    # Define los nombres de las columnas del archivo CSV
    campos = [
        "Departamento",
        "Poblacion",
        "Ingreso",
        "Numero_hogares",
        "Actividad_principal"
    ]

    # Crear el escritor del archivo CSV
    escritor = csv.DictWriter(
        archivo,
        fieldnames=campos
    )

    # Escribe los encabezados del archivo
    escritor.writeheader()

    # Escribe datos de los cinco departamentos
    escritor.writerows(datos)

# Confirma que el archivo fue creado correctamente
print("Archivo datos_economicos.csv creado correctamente.")