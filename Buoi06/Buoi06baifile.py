# Bước 1: Doc file ban dau 
with open("PTPYTHON/Buoi06/Text.txt", "r", encoding="utf-8") as f:    text = f.read()

# Bước 2: nen du lieu
compressed = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        compressed += text[i-1] + str(count)
        count = 1

compressed += text[-1] + str(count)

# ghi file nén
with open("compressed.txt", "w", encoding="utf-8") as f:
    f.write(compressed)

print("Đã nén xong:")
print(compressed)


#Bước 3:Doc Filee nen va khoi phuc
with open("compressed.txt", "r", encoding="utf-8") as f:
    data = f.read()

decompressed = ""
i = 0

while i < len(data):
    char = data[i]
    i += 1

    num = ""
    while i < len(data) and data[i].isdigit():
        num += data[i]
        i += 1

    decompressed += char * int(num)

# ghi file 
with open("restore.txt", "w", encoding="utf-8") as f:
    f.write(decompressed)

print("\nĐã khôi phục:")
print(decompressed)