# Keyla Paola NC = 0033

import cv2
import numpy as np
import os

# Cargar imagen
imagen = cv2.imread("lobo.p10.jpg")

# Verificar que la imagen exista
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes
bordes = cv2.Canny(gris, 50, 150)

# Detectar líneas mediante Hough
lineas = cv2.HoughLinesP(
    bordes,
    1,
    np.pi / 180,
    threshold=50,
    minLineLength=50,
    maxLineGap=10
)

# Crear copia de la imagen
resultado = imagen.copy()

# Dibujar líneas
if lineas is not None:

    for linea in lineas:

        # Obtener los 4 puntos de la línea
        puntos = np.array(linea).reshape(-1)

        if len(puntos) >= 4:
            x1, y1, x2, y2 = puntos[:4]

            cv2.line(
                resultado,
                (int(x1), int(y1)),
                (int(x2), int(y2)),
                (0, 0, 255),
                2
            )

# Mostrar resultados
cv2.imshow("Imagen original 0033", imagen)
cv2.imshow("Bordes 0033", bordes)
cv2.imshow("Lineas detectadas 0033", resultado)

# Crear carpeta resultados si no existe
os.makedirs("../resultados", exist_ok=True)

# Guardar resultado
ruta = "../resultados/ejemplo1_lineas.jpg"
cv2.imwrite(ruta, resultado)

print("Deteccion de lineas terminada.")

if lineas is not None:
    print("Cantidad de segmentos detectados:", len(lineas))
else:
    print("No se detectaron lineas.")

print("Resultado guardado en:")
print(ruta)

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()


print("Keyla Paola NC = 0033")