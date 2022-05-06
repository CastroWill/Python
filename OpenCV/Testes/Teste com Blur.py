import cv2
import numpy as np

img = cv2.imread("olho.jpg")

copia = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#suave = cv2.GaussianBlur(copia, (7, 7), 0) # aplica blur 
suave = cv2.GaussianBlur(gray,(21,21),0)

(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(copia,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

cv2.imshow("Imagem Binarizada", bin)

canny1 = cv2.Canny(bin, 100, 100)
canny2 = cv2.Canny(bin, 70, 120)


resultado = np.hstack([gray, suave])
resultado1 = np.hstack([canny1, canny2])



cv2.imshow("Imagem com com Blur", resultado)
cv2.imshow("Imagem com Canny 1 e 2", resultado1)


cv2.waitKey(0)
cv2.destroyAllWindows()
