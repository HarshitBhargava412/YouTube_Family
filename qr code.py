import qrcode

img = qrcode.make("link to be converted")

img.save("name.png")

img.show()

# this would create the qr code you required for opening the given link.