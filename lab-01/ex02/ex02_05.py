so_gio = float(input("Nhập số giờ làm việc trong tuần: "))
luong_gio = float(input("Nhập mức lương theo giờ: "))
if so_gio <= 44:
    tien_luong = so_gio * luong_gio
else:
    tien_luong = 44 * luong_gio + (so_gio - 44) * luong_gio * 1.5
print("Số tiền thực nhận:", tien_luong)
