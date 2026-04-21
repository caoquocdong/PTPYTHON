s = input("Nhap chuoi: ")
s = s.strip()# Xóa khoảng trắng đầu cuối
words = s.split()# Tách thành từng từ (tự loại bỏ nhiều space)
s = " ".join(words)#Ghép lại thành chuỗi chuẩn (1 space)
s = s.replace(" ,", ",")#Xử lý dấu phẩy, dấu chấm (xóa khoảng trắng trước nó)
s = s.replace(" .", ".")
print("Chuoi sau khi sua:", s)