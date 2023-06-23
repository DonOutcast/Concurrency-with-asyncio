
def is_palindrome(string):
    return string.strip() == string[::-1].strip()


if __name__ == "__main__":
    user_word = input()
    result = is_palindrome(user_word)
    print(result)
