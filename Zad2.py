import matplotlib.pyplot as plt
import cv2
import urllib.request

regularurl = urllib.request.urlopen('https://commons.wikimedia.org/wiki/File:Overexposed_photo.JPG')
photo = cv2.imdecode(regularurl, cv2.IMREAD_COLOR)

regular = cv2.imread('Lemon.jpg')
overexposed = cv2.imread('overexposed.JPG')
underexposed = cv2.imread('underexposed.jpg')
regular_rgb = cv2.cvtColor(regular, cv2.COLOR_BGR2RGB)
overexposed_rgb = cv2.cvtColor(overexposed, cv2.COLOR_BGR2RGB)
underexposed_rgb = cv2.cvtColor(underexposed, cv2.COLOR_BGR2RGB)

plt.imshow(photo)
plt.show()

# plt.imshow(regular_rgb)
# plt.show()
# plt.imshow(overexposed_rgb)
# plt.show()
# plt.imshow(underexposed_rgb)
# plt.show()