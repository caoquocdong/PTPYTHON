menhgia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

def nhaptien():

    a = int(input("Nhap so tien Hang can tra: "))
    b = int(input("Nhap so tien Hang Khach da tra: "))
    return a, b

def DKTien(a, b):
#Khach dua thieu tien
    if b < a:
        print("Khách còn thiếu", a - b)
# khách dua dung tien
    elif b == a:
        print("Cảm ơn khách hàng. Hẹn gặp lại")
# khach dua dư tien
    else:
        tienthoi = b - a
        print("Tiền thối lại là:", tienthoi)
        tinhtien(tienthoi)
        input("Nhấn Enter để kết thúc...")
        print("Cảm ơn khách hàng. Hẹn gặp lại")

def tinhtien(tien):
    tong = 0
    soloai = 0
    print("So tien duoc doi thanh:")
    for i in menhgia:
        soto = tien // i
        tien = tien % i
        if soto > 0:
            soloai += 1
            #chổ này khác là đưa vào if để in ra gọn hơn chứ 
            #ko cần in ra loại nào 0 tờ
            tong += soto
            print ("Loại ",i," gồm ",soto," tờ")
    print("TỔNG CỘNG CÓ", tong, "TỜ")
    print("Tong so loai tờ là ", soloai)

def main():
    a, b = nhaptien()
    DKTien(a, b)

main()