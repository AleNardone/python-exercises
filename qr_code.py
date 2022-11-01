
#Code QR
import qrcode

#Encode QR
from pyzbar.pyzbar import decode
from PIL import Image

#Code QR
data = 'PUT LINK HERE OR WRITE A MESSAGE'
qr = qrcode.QRCode(version = 1)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('WRITE FILE LOCATION YOU WANT TO SAVE YOUR QR IMAGE HERE')

#Encode QR
img = Image.open('WRITE FILE LOCATION YOU SAVED YOUR QR IMAGE HERE')
result = decode(img)
print(result)

