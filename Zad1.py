import matplotlib.pyplot as plt
import cv2

# Ścieżka do obrazu z wykorzysatniem biblioteki OpenCV
img = cv2.imread('Lemon.jpg')

#  Wyświetlenie obrazu za pomocą matplotlib
plt.imshow(img)
plt.show()
