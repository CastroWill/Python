import cv2
import numpy as np

eye = cv2.imread('olho2.jpg')
eyec = eye.copy()

print (eyec.shape)

gray_img = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)

#Aplicando thresholding dinâmico
img = cv2.medianBlur(gray_img,5)


ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

circles	= cv2.HoughCircles(th3,cv2.HOUGH_GRADIENT, 1, 120,param1=100,param2=30,minRadius=40,maxRadius=65)
circles	= np.uint16(np.around(circles))
 
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(eye,(i[0],i[1]),i[2],(0,255,0), 2)
    #draw the center of the circle
    cv2.circle(eye,(i[0],i[1]),2,(0,0,255),5)

cv2.imshow("Imagem Original", eyec)
cv2.imshow("Imagem Preto e Branco", gray_img)
cv2.imshow("Imagem com Blur", img)
cv2.imshow("Circulos reconhecidos", eye)


cv2.waitKey(0)
cv2.destroyAllWindows()
