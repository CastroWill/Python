import cv2
import numpy as np
from matplotlib import pyplot as plt

eye = cv2.imread('olho2.jpg')
eyec = eye.copy()

gray_img = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)


img = cv2.medianBlur(gray_img,5)

#Aplicando thresholding dinâmico
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

cv2.imshow("Imagens", np.hstack([img, th1, th2, th3]))


cv2.waitKey(0)
cv2.destroyAllWindows()

