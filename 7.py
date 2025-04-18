# Chuyển đổi nhiệt độ
def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Chọn chuyển đổi (1: C->F, 2: F->C): ")
if choice == "1":
    c = float(input("Nhập độ C: "))
    print(f"{c}°C = {c_to_f(c)}°F")
elif choice == "2":
    f = float(input("Nhập độ F: "))
    print(f"{f}°F = {f_to_c(f)}°C")
else:
    print("Lựa chọn không hợp lệ!")