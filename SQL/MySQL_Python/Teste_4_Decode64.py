import base64

with open("luis.png", "rb") as imageFile:
    imgs = base64.b64encode(imageFile.read())

fh = open("LuisDecode.png", "wb")
fh.write(base64.b64decode(imgs))
fh.close()
