# Kiểm tra chuỗi đối xứng
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

word = input("Nhập chuỗi: ")
if is_palindrome(word):
    print(f'"{word}" là chuỗi đối xứng')
else:
    print(f'"{word}" không phải chuỗi đối xứng')