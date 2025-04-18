# Quản lý danh sách
items = []

while True:
    print("\n1. Thêm mục\n2. Xóa mục\n3. Hiển thị danh sách\n4. Thoát")
    choice = input("Chọn: ")
    
    if choice == "1":
        item = input("Nhập mục: ")
        items.append(item)
    elif choice == "2":
        item = input("Nhập mục cần xóa: ")
        if item in items:
            items.remove(item)
        else:
            print("Mục không tồn tại!")
    elif choice == "3":
        print("Danh sách:", items)
    elif choice == "4":
        break
    else:
        print("Lựa chọn không hợp lệ!")