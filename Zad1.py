import matplotlib.pyplot as plt
from PIL import Image

# Ścieżka do obrazu
img = Image.open('Lemon.jpg')

#  Wyświetlenie obrazu za pomocą matplotlib
plt.imshow(img)
plt.show()
