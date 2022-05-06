
import cv2

cont = 0
arqCasc1 = 'haarcascade_frontalface_default.xml'
arqCasc2 = 'haarcascade_eye.xml'
faceCascade1 = cv2.CascadeClassifier(arqCasc1) #classificador para o rosto
faceCascade2 = cv2.CascadeClassifier(arqCasc2) #classificador para os olhos
 
webcam = cv2.VideoCapture(0)  #instancia o uso da webcam
 
while True:
    s, imagem = webcam.read() #pega efeticamente a imagem da webcam
    imagem = cv2.flip(imagem,180) #espelha a imagem
    
    """
    faces = faceCascade1.detectMultiScale(
        imagem,
        minNeighbors=20,
        minSize=(30, 30),
	maxSize=(300,300)
    )
    """
    
   
    olhos = faceCascade2.detectMultiScale(
        imagem,
        minNeighbors=20,
        minSize=(200, 200),
	maxSize=(1000,1000)
    )
 
    # Desenha um retangulo nas faces e olhos detectados
    #for (x, y, w, h) in faces:
        #cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 4)

    if cont < 2:
        
        for (x, y, w, h) in olhos:
            cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)
            eye = imagem[olhos[0][1]:olhos[0][1]+olhos[0][3],olhos[0][0]:olhos[0][0]+olhos[0][2]]
            
            
        if cv2.waitKey(1) & 0xFF == ord('e'):
            
            if cont == 0:
                cv2.imwrite("olhoD.jpeg",eye)
                

            if cont == 1:
                cv2.imwrite("olhoE.jpeg",eye)
                
            cont+=1
            
        cv2.imshow('Video', imagem) #mostra a imagem captura na janela
    else:

        break
            
        
 
    #o trecho seguinte e apenas para parar o codigo e fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas abertas
