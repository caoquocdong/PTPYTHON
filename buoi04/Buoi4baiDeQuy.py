def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)
n = int(input("Nhap n: "))
print("n! =", giaithua(n))

def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)
n = int(input("Nhap n: "))
print("n! =", giaithua(n))

def luythua(a, b):
    if b == 0:
        return 1
    return a * luythua(a, b - 1)
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print("a^b =", luythua(a, b))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print("UCLN =", gcd(a, b))
