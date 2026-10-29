import matplotlib.pyplot as plt
import cv2

# Ścieżka do obrazu z wykorzysatniem biblioteki OpenCV
img = cv2.imread('Lemon.jpg')
# Konwersja z BGR na RGB dla naturalności kolorów
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#  Wyświetlenie obrazu za pomocą matplotlib
plt.imshow(img_rgb)
plt.show()
