chuoi = input("Nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")
ket_qua = []
for so in chuoi.split(","):
    so = so.strip()
    if int(so, 2) % 5 == 0:
        ket_qua.append(so)
print(",".join(ket_qua))
