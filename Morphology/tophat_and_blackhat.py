import cv2
import numpy as np
import os

path = os.path.join('./Morphology/image/Moon.jpg')
img = cv2.imread(path)

kernel = np.ones((12,12), np.uint8)
tophat_result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat_result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original", cv2.resize(img, (500,500)))
cv2.imshow("Tophat Result", cv2.resize(tophat_result, (500,500)))
cv2.imshow("Blackhat Result", cv2.resize(blackhat_result, (500,500)))

cv2.waitKey(0)
cv2.destroyAllWindows()