import cv2

stream = cv2.VideoCapture('http://192.168.50.26:4747/video')

# Use the next line if your camera has a username and password
# stream = cv2.VideoCapture('protocol://username:password@IP:port/1')  

while True:

    r, f = stream.read()
    cv2.imshow("IP Camera stream",f)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break


