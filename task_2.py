from collections import deque

def is_palindrome(text):
    normalized_text = text.lower().replace(" ", "")
    characters = deque(normalized_text)
    while len(characters) > 1:
        if characters.pop() != characters.popleft():
            print(f"'{text}' is not a palindrome")
            break
    else:
        print(f"'{text}' is  a palindrome")

if __name__ == "__main__":
    user_input = 'y'
    print("Welcome to Palindrome Game!")
    print("I will help to you to check whether something is a palindrome")
    print("or not")

    while user_input == 'y':
        checked_text = input("Please write your text \n")
        is_palindrome(checked_text)
        user_input = input("Do you want to continue? y / n ")




