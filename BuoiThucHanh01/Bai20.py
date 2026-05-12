menhgia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

def nhaptien():
    tien = int(input("Nhập số tiền: "))
    return tien

def tinhtien(tien):
    tong = 0
    soloai=0
    print("So tien duoc doi thanh:")
    for i in menhgia:
        soto = tien // i
        if soto > 0 :
            soloai+=1
        tien = tien % i
        tong += soto
        print("Loai", i, "gom", soto, "to")
    print("TỔNG CỘNG CÓ", tong, "TỜ")
    print("Tong so loai = ",soloai)

def main():
    tien = nhaptien()
    tinhtien(tien)

main()