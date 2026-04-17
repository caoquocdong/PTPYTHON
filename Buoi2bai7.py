n = int(input("Hãy nhập n: "))
Somayman = True
while n > 0:
    layso = n % 10
    if layso == 6 or layso == 8:
        Somayman = True
    else:
        Somayman = False
        break  
    n //= 10
if Somayman:
    print("Vậy đây là số may mắn")
else:
    print("Đây không là số may mắn")