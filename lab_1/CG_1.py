import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi'] # Укажите шрифт по умолчанию
plt.rcParams['axes.unicode_minus'] = False # Решить проблему, что знак минус '-' отображается в виде квадрата на сохраненном изображении

img_gray0 = cv2.imread("lab_1\\bird2.jpg", cv2.IMREAD_GRAYSCALE)
img_gray0 = 255 - img_gray0
h, w= img_gray0.shape


plt.figure()
plt.imshow(img_gray0, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
plt.title("Исходное изображение")

img_gray_eq = img_gray0

img_dither = np.zeros((h+1, w+1), dtype=np.float64)
img_undither = np.zeros((h, w), dtype=np.uint8)

threshold = 128

for i in range(h):
    for j in range(w):
        img_dither[i, j] = img_gray_eq[i, j]
        if img_gray_eq[i, j] > threshold:
            img_undither[i, j] = 255

for i in range(h):
    for j in range(w):
        old_pix = img_dither[i, j]
        if (img_dither[i, j] > threshold):
            new_pix = 255
        else:
            new_pix = 0

        img_dither[i, j] = new_pix

        quant_err = old_pix - new_pix

        if j > 0:
            img_dither[i+1, j-1] = img_dither[i+1, j-1] + quant_err * 3 / 16
        img_dither[i+1, j] = img_dither[i+1, j] + quant_err * 5 / 16
        img_dither[i, j+1] = img_dither[i, j+1] + quant_err * 7 / 16
        img_dither[i+1, j+1] = img_dither[i+1, j+1] + quant_err * 1 / 16

img_dither = img_dither.astype(np.uint8)
img_dither = img_dither[0:h, 0:w]

plt.figure()
plt.imshow(img_dither, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
plt.title("dither")

plt.figure()
plt.imshow(img_undither, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
plt.title("undither")

plt.show()
