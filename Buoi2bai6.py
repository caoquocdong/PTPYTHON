n = int(input("hãy nhập n:"))
Max = 0
while (n>0):
    layso = n%10
    if Max < layso:
      Max = layso
    n//=10
print("Số lớn nhất là : ",Max)
        