def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

chuoi = input("Nhập chuỗi: ")
print("Chuỗi đảo ngược:", dao_nguoc_chuoi(chuoi))
