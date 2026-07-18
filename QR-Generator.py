import qrcode

data = input("Enter text or URL to generate QR code: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image()

file_name = input("Enter file name: ") + ".png"
image.save(file_name)