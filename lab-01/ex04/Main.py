from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("1. Them sinh vien.")
    print("2. Cap nhat thong tin sinh vien boi ID.")
    print("3. Xoa sinh vien boi ID.")
    print("4. Tim kiem sinh vien theo ten.")
    print("5. Sap xep sinh vien theo diem trung binh.")
    print("6. Sap xep sinh vien theo ten chuyen nganh.")
    print("7. Hien thi danh sach sinh vien.")
    print("0. Thoat.")
    key = int(input("Nhap tuy chon: "))
    if key == 0:
        print("Ban da chon thoat chuong trinh!")
        break
    elif key == 1:
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong!")
    elif key in range(2, 8):
        if qlsv.soLuongSinhVien() == 0:
            print("Danh sach sinh vien trong!")
        elif key == 2:
            ID = int(input("Nhap ID: "))
            qlsv.updateSinhVien(ID)
        elif key == 3:
            ID = int(input("Nhap ID: "))
            if qlsv.deleteById(ID):
                print("Sinh vien co ID =", ID, "da bi xoa.")
            else:
                print("Sinh vien co ID =", ID, "khong ton tai.")
        elif key == 4:
            name = input("Nhap ten de tim kiem: ")
            qlsv.showSinhVien(qlsv.findByName(name))
        elif key == 5:
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        elif key == 6:
            qlsv.sortByMajor()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        elif key == 7:
            qlsv.showSinhVien(qlsv.getListSinhVien())
    else:
        print("Khong co chuc nang nay! Hay chon lai.")
