import qrcode
from PIL import Image

#features of qrcode image
features = qrcode.QRCode(version=1,box_size=40,border=5)

#input website url & file name
url = input('Enter the URL/Text:')
file_name = input('Enter file name:') +  '.png'

#passing content to qrcode
features.add_data(url)

#fitting the qrcode image in features
features.make(fit=True)

#generate qrcode
qr_img = features.make_image(fill_colour = 'black', back_colour = 'white')

#save qrcode
qr_img.save(file_name)
