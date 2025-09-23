#Lập trình bằng Python trên Github.
#Trong thuật toán RSA, cho p=17, q=23, e=5. Thực hiện mã hóa thông điệp P=TenCuaBan.
p = 17
q = 23
e = 5
n = p * q

#Thông điệp cần mã hóa
P = "NguyenNgocTuyetNhi"

#Đổi sang số ASCII
M = [ord(c) for c in P]
#Mã hóa RSA
C = [pow(m, e, n) for m in M]

print("P:", P)
print("ASCII:", M)
print("RSA:", C)
