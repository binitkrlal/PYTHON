import qrcode


url = input("enter the link or url")

img = qrcode.make(url)

img.save('qrcode.png')

print("QR code genrated Sucessfully")
