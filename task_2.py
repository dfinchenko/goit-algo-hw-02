from collections import deque

def is_palindrome(s):
    formatted_str = ''.join(char.lower() for char in s if char.isalnum())
    char_deque = deque(formatted_str)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Отримання рядка від користувача
user_input = input("Введіть рядок, щоб перевірити чи є паліндромом: ")

# Перевірка, чи є рядок паліндромом
is_palindrome_result = is_palindrome(user_input)
print(f"'{user_input}' - рядок є паліндромом: {is_palindrome_result}")