# Nhap nhieu dong; nhap dong trong de ket thuc
cac_dong = []
while True:
    dong = input()
    if dong == "":
        break
    cac_dong.append(dong.upper())
for dong in cac_dong:
    print(dong)
