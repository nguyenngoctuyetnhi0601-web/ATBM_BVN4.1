
#Cho k=39, và Plaintext = NGUYEN NGOC TUYET NHI. Hãy mã hóa theo thuật toán Ceasar.

def caesar(ten, k):
    ketqua = ""
    for kytu in ten:
        if kytu.isalpha():
            base = ord('A') if kytu.isupper() else ord('a')
            ketqua += chr((ord(kytu) - base + k) % 26 + base)
        else:
            ketqua += kytu
    return ketqua

print("Mã hoá với tên NGUYỄN NGỌC TUYẾT NHI: ",caesar("NGUYEN NGOC TUYET NHI", 39)) 



