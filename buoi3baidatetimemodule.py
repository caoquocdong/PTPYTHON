from datetime import datetime

Homnay = datetime.now()

print("Năm hiện tại:", Homnay.year)
print("Tháng hiện tại (bằng chữ):", Homnay.strftime("%B"))
print("Tuần thứ mấy trong năm:", Homnay.strftime("%U"))
print("Tuần thứ mấy trong tháng:", (Homnay.day - 1)//7 + 1)
print("Ngày thứ mấy trong năm:", Homnay.strftime("%j"))
print("Ngày hiện tại:", Homnay.day)
print("Thứ hiện tại:", Homnay.strftime("%A"))
print("Giờ phút giây:", Homnay.strftime("%H:%M:%S"))