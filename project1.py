#máy tính tiền siêu thị với 1 số sản phẩm :
def so_tien_san_pham(giatien):
    return sum(giatien)
def tien_thoi(giaTien,khachTra):
    if giaTien > khachTra :
        return -1
    else :
        return khachTra-giaTien
def main():
    # cac san pham : apple = 15 , banh mi = 10 , mi tom =5, keo= 20
    mang = []
    n = int(input("nhap so san pham can mua : "))
    for i in range(n):
        ten_san_pham = input(f"phan tu {i+1}:")
        mang.append(ten_san_pham)
    print(mang)
    list1 = []
    list2 = []
    for i in range(n) :
        tong_so_luong = int(input(f"so luong cua san pham {i+1} : "))
        list1.append(tong_so_luong)
    for i in range(n) :
        tong_so_tien = int(input(f"so tien cua san pham {i+1} : "))
        list2.append(tong_so_tien)
    list3 = [list1*list2 for list1,list2 in zip(list1,list2)]

    
    
    so_tienSP = so_tien_san_pham(list3)
    khach_tra = float(input("nhap so tien khach tra : "))
    tienThoi = tien_thoi(so_tienSP,khach_tra)
    print(f"so tien san pham la : {so_tienSP}")
    print(f"so tien thua tra cho khach : {tienThoi}")
    
main()


