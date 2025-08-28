import cv2
import numpy as np
import matplotlib.pyplot as plt

# crea una imagen 256x256 con un círculo blanco
img = np.zeros((256, 256, 3), dtype=np.uint8)
cv2.circle(img, center=(128, 128), radius=60, color=(255, 255, 255), thickness=-1)

# convierte BGR→RGB para mostrar con Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.title("Prueba OpenCV + NumPy + Matplotlib")
plt.imshow(img_rgb)
plt.axis('off')
plt.show()