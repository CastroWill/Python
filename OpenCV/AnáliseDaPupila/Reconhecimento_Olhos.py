import cv2
import numpy as np

# Xml de classificacao da OpenCV
classification = "haarcascade_eye_tree_eyeglasses.xml"

# Setando a classificacao do xml da OpenCV para olhos
faceCascade = cv2.CascadeClassifier(classification)

# Ler a imagem
image = cv2.imread("luis.jpeg")

# Converte para cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""
# Fazer a deteccao dos olhos na imagem
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Setar o retangulo amarelo
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 210), 2)
"""

# Exibir a imagem
cv2.imshow("imagem", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


