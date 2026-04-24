#bài 1 tính tổng các chữ số trong n.
def tong_chu_so(n):
    if n == 0:   # điều kiện dừng
        return 0
    return n % 10 + tong_chu_so(n // 10)
n = int(input("Nhap n: "))
print("Tong chu so co trong n =", tong_chu_so(n))

##bai2 tính guaiii thừa của n
def giaithua(n):
    if n == 1:
        return 1
    return giaithua(n - 1) * n
n = int(input("Nhap n: "))
print("n! =", giaithua(n))

#bai 3 tinh a^b 
def luythua(a, b):
    if b == 0:
        return 1
    return luythua(a, b - 1) * 
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print("a^b =", luythua(a, b))

#Bai 4 UCLN cua a b
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print("UCLN =", gcd(a, b))
