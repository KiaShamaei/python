#Import Library
import qrcode
#Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://businessmoshaver.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black")
img.save("medium.png")