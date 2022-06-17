import cv2
import numpy as np
import os

path = os.path.join('./Morphology/image/Son.jpg')
img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)

kernel = np.ones((3,3), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("Original", cv2.resize(img, (500,500)))
cv2.imshow("Gradient Result", cv2.resize(result, (500,500)))

cv2.waitKey(0)
cv2.destroyAllWindows()