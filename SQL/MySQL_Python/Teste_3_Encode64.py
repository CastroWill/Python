import base64
 
with open("luis.png", "rb") as imageFile:
    img = base64.b64encode(imageFile.read())
    img = str(img)
    print (img)
