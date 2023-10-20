import pywhatkit

Ph_no = input("Enter Phone Number: ")
msg = input("Enter Message: ")
hr = int(input("Hour: "))
mins = int(input("Minute: "))
pywhatkit.sendwhatmsg(Ph_no,msg,hr,mins)
print("Done!")
