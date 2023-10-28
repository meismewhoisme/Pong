import os
#os.system('cmd /k "date"') 

place = input("Who to")
text = input("What to send:")
if len(text) < 16:
    text = text.ljust(16)
print(text)
encodedtext = "".join(hex(ord(v)).split("x")[1] for v in text[:16])
print(encodedtext)
os.system(f"cmd /k ping -p '{encodedtext}' -c 1 {place}") 