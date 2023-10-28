import os
#os.system('cmd /k "date"') 

text = input("What to send:")
if len(text) < 16:
    text = text.ljust(16)
print(text)
encodedtext = "".join(hex(ord(text[:16])))
print(encodedtext)