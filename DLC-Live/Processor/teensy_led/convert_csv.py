import numpy as np
import csv

# cargar un archivo NPY
arr = np.load('DLC-Live\Saved Data LED\Webi_Tarea2_2023-03-11_2_TS.npy')

# crear un archivo CSV y escribir los datos
with open('archivo.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in arr:
        writer.writerow(row)