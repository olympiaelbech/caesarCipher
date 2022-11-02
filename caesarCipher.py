key = int(input())
plainText = str(input())
text = plainText.upper()
cipher = ''

for i in text:
    if 65 <= ord(i) <= 90:
        encryption = ord(i) + key
        while encryption < 65:
            encryption += 26
        while encryption > 90:
            encryption -= 26
        i = chr(encryption)
    cipher += i

print(cipher)