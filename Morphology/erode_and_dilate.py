import os 
import cv2
import numpy as np

path = os.path.join('./Morphology/image/j.jpg')
img = cv2.imread(path)

k = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

erosion_1 = cv2.erode(img, k)
erosion_2 = cv2.erode(erosion_1, k)
erosion_3 = cv2.erode(erosion_2, k)

dilation_1 = cv2.dilate(img, k)
dilation_2 = cv2.dilate(dilation_1, k)
dilation_3 = cv2.dilate(dilation_2, k)

merged_erosion = np.hstack((img, erosion_1, erosion_2, erosion_3))
merged_dilation = np.hstack((img, dilation_1, dilation_2, dilation_3))

cv2.imshow('Erosion', merged_erosion)
cv2.imshow('Dilation', merged_dilation)


cv2.waitKey(0)
cv2.destroyAllWindows()
