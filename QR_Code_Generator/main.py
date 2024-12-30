import qrcode

data = input("URL: ").strip()
filename = input("Enter file name(also include format): ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(file_color = 'black', back_color = 'white')
image.save (filename)
print(f"QR code saved as {filename} ")