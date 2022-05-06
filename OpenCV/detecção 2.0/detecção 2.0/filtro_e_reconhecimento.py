import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('olhoD.jpeg')

#Filtro para imagem
def filtro(img):
    
    #Conversão para escala de cinza
    cinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #smooth
    blur = cv2.medianBlur(cinza,8)
    

    return blur

#Reconhece o circulo
def circulo(blurR):

    circles = cv2.HoughCircles(blurR, cv2.HOUGH_GRADIENT, 2, 500, param1=100, param2=25, minRadius=5, maxRadius=32)


    if circles is not None:
        
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(blur1,(i[0],i[1]),i[2],(0,255,0), 1)
            #draw the center of the circle
            cv2.circle(blur1,(i[0],i[1]),2,(0,0,255),5)

            #Mostra o raio do círculo convertido para milímetros.
            radm = i[2]
            print(radm*0.264583333333334, "mm")
    else:
        print('Circulo não encontrado')
        

    return blurR





blur1 = filtro(img)
circleR = circulo(blur1)
cv2.imshow('teste',blur1)
cv2.waitKey(0)
cv2.destroyAllWindows()



