import qrcode

user=input("enter your name and phone number:  ")

x=qrcode.make(user)
x.save("qr1.png")