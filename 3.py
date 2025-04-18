# Đọc nội dung file text
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("Nội dung file:")
        print(content)
except FileNotFoundError:
    print("File không tồn tại!")