# Máy tính cơ bản
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Không chia được cho 0"
    else:
        return "Phép toán không hợp lệ"

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
op = input("Nhập phép toán (+, -, *, /): ")
print(f"Kết quả: {calculator(a, b, op)}")