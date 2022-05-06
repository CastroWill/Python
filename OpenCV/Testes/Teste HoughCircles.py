import cv2
import numpy as np
 
#Carrega a imagem
planets	= cv2.imread('planets.jpg')

#Converte para tons de cinza
gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)

#Aplica blur para suavizar a imagem
img = cv2.medianBlur(gray_img, 5)

#Converte a imagem de volta para RGB
#cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
 
 
circles	= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 1, 120,param1=100,param2=30,minRadius=0,maxRadius=100)
circles	= np.uint16(np.around(circles))
 
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0), 2)
    #draw the center of the circle
    cv2.circle(planets,(i[0],i[1]),2,(0,0,255),5)
 
cv2.imshow("HoughCirlces", planets)
cv2.waitKey()
cv2.destroyAllWindows()
