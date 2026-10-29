import matplotlib.pyplot as plt
import cv2
# 1.
# Ścieżka do obrazu z wykorzysatniem biblioteki OpenCV
img = cv2.imread('Lemon.jpg')
# Konwersja z BGR na RGB dla naturalności kolorów
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2.
#  Wyświetlenie obrazu za pomocą matplotlib
plt.imshow(img_rgb)
plt.show()
# Wyświetla wymiary i kanały obrazu (wyskość, szerokość, l.kanałów)
print(img_rgb.shape)
# 3. 
# Dzieki shape możemy zmienić wymiary obrazu
new_height = int(img_rgb.shape[0] * 0.5)
new_width = int(img_rgb.shape[1] * 0.5)
# Wprowadzamy zmiany wymiarowe
resized_img = cv2.resize(
    img_rgb, (new_width, new_height)
)
print(resized_img.shape)
plt.imshow(resized_img)
plt.show()