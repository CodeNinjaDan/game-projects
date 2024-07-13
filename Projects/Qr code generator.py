
import qrcode

data = '[Check out this cool website]' '(https://cristianoronaldo.com/#cr7)'

qr =  qrcode.QRCode(version = 1, box_size = 10, border  = 5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('c:/Users/MTEJA/Desktop/py4e/New folder/Myqrcode1.png')
