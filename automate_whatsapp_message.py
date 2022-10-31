import pywhatkit

#Phone number with country code, message, hour and minutes
#You can also levae it like that and whatsapp web will open instantly
try:
    pywhatkit.sendwhatmsg_instantly("+xxxxxxxxx",
                                    "Hi")
    print("Successfully sent!")
except:
    print("Unexpected error!")


