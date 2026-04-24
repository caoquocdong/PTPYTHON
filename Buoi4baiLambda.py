import math

# a
print('Nhap gia tri n : ')
n = int(input())
Giatrituyetdoi = lambda n: abs(n)
print('Gia tri tuyet doi cua n la : ', Giatrituyetdoi(n))

# b
print('Nhap gia tri n de cong voi 15: ')
n = int(input())
Hamcong15 = lambda n: n + 15
print('Gia tri cua n + 15 la : ', Hamcong15(n))

# c
print('Nhap hai doi so x va y : ')
x = int(input('Nhap gia tri x: '))
y = int(input('Nhap gia tri y: '))
Tich = lambda x, y: x * y
print('Tich cua x va y la : ', Tich(x, y))

# d
print('Nhap gia tri n co la boi so cua 13 hoac 19 : ')
n = int(input())
BoiSo = lambda n: (n % 13 == 0) or (n % 19 == 0)
if BoiSo(n):
    print(n, "la boi so cua 13 hoac 19")
else:
    print(n, "khong phai la boi so cua 13 hoac 19")

# e
print('Nhap ban kinh r : ')
r = float(input())
Dientich = lambda r: math.pi * r**2
print('Dien tich cua hinh tron la : ', Dientich(r))

# f 
print('Nhap chieu dai d va chieu rong r cua hinh chu nhat ')
d = float(input('Nhap chieu dai d: '))
rong = float(input('Nhap chieu rong r: '))
ChuVi = lambda d, rong: 2 * (d + rong)
print('Chu vi hinh chu nhat la : ', ChuVi(d, rong))

# g
print('Nhap gia tri so nguyen n de kiem tra so chinh phuong: ')
n = int(input())
SoChinhPhuong = lambda n: int(math.sqrt(n))**2 == n
if SoChinhPhuong(n):
    print(n, "la so chinh phuong")
else:
    print(n, "khong phai la so chinh phuong")

# h
print('Nhap gia tri n de kiem tra so nguyen to: ')
n = int(input())

def SoNguyenTo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

annofuction = lambda n: SoNguyenTo(n)

if annofuction(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong phai la so nguyen to")