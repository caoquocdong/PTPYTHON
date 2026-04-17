n = int(input("hãy nhập n:"))
tong = 0
tich = 1
while (n>0):
    layso = n%10
    tich *=layso
    tong += layso
    n//=10
print("Số tong là : ",tong)
print("Số chan là : ",tich)
        