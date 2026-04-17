n = int(input("hãy nhập n:"))
chan = 0
le = 0
while (n>0):
    layso = n%10
    if layso%2==0:
        chan+=1
    else: 
        le+=1
    n//=10
print("Số chẳn là : ",chan)
print("Số lẻ là : ",le)
        