def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập một số nguyên: "))
if la_so_nguyen_to(n):
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải là số nguyên tố.")
