import qrcode as qr
from PIL import Image

# Create a QR code instance

qr = qr.QRCode(version=1,
               error_correction=qr.constants.ERROR_CORRECT_H,
                box_size=10, border=5)

qr.add_data("https://github.com/khuhrohumayun")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR_Generator.png")




