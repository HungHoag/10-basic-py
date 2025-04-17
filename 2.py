# Trò chơi đoán số
import random

number = random.randint(1, 100)
attempts = 0

print("Hãy đoán số từ 1 đến 100!")
while True:
    guess = int(input("Nhập số: "))
    attempts += 1
    if guess < number:
        print("Số lớn hơn!")
    elif guess > number:
        print("Số nhỏ hơn!")
    else:
        print(f"Chúc mừng! Bạn đoán đúng sau {attempts} lần.")
        break