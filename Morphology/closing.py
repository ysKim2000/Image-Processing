import cv2
import numpy as np
import os

path = os.path.join('./Morphology/image/man.png')
img = cv2.imread(path)

kernel = np.ones((11,11), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original", cv2.resize(img, (500,500)))
cv2.imshow("Closing Result", cv2.resize(result, (500,500)))

cv2.waitKey(0)
cv2.destroyAllWindows()