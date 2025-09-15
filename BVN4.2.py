#Mã hóa thay thế bằng phép toán cộng với k=39 theo danh sách. Plaintext là P=Nguyen Ngoc Tuyet Nhi. Thep Z26.
def ceasar_encrypt(plaintext, k):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else: 
                base = ord('a')
            new_char = chr((ord(ch) - base + k) % 26 + base)
            ciphertext += new_char
        else:
            ciphertext += ch
    return ciphertext

print("Mã hoá với tên NGUYỄN NGỌC TUYẾT NHI:", ceasar_encrypt("Nguyen Ngoc Tuyet Nhi", 39))
