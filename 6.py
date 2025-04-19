# Đồng hồ 
import time
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình
    print("Thời gian hiện tại:", time.strftime("%H:%M:%S"))
    time.sleep(1)