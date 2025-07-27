import datetime
import os

# Obtener la fecha de ayer
ayer = datetime.date.today() - datetime.timedelta(days=1)
fecha_str = ayer.strftime("%d")  # Solo el día, por ejemplo "26"

# Nombres de los archivos
archivo1 = f"archivo_{fecha_str}.txt"
archivo2 = f"archivo_{fecha_str}_b.txt"

# Crear y escribir en los archivos
with open(archivo1, "w") as f1:
    f1.write(f"Este es el archivo {archivo1}, creado el {ayer}\n")

with open(archivo2, "w") as f2:
    f2.write(f"Este es el archivo {archivo2}, creado el {ayer}\n")

print(f"Archivos creados: {archivo1} y {archivo2}")
