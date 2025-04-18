# Ghi nội dung vào file text
content = input("Nhập nội dung để ghi vào file: ")
with open("output.txt", "w") as file:
    file.write(content)
print("Đã ghi nội dung vào output.txt")