from datetime import datetime

Homnay = datetime.now()

print("nam hien tai:", Homnay.year)
print("thangg Hienn tai bang chu:", Homnay.strftime("%B"))
print("Tuan thu may trong nam:", Homnay.strftime("%U"))
print("Tuan thu may trong thang:", (Homnay.day - 1)//7 + 1)#tinh tuan thu may thang
print("Ngày thu may trong nam:", Homnay.strftime("%j"))
print("Ngày hien tai:", Homnay.day)
print("Thu hien tai:", Homnay.strftime("%A"))
print("Gio phut giay 5s :", Homnay.strftime("%H:%M:%S"))