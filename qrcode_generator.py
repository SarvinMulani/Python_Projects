import qrcode 

def qrcode_generator():
    try:
        link = input("Paste the link here: ")
        img = qrcode.make(link)
        name = input("File Name: ")
        img.save(name)
    except:
        print("ERROR!")

qrcode_generator()