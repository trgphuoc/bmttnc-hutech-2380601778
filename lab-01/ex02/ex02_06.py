x = int(input("Nhập X: "))
y = int(input("Nhập Y: "))
mang = [[i * j for j in range(y)] for i in range(x)]
print(mang)
