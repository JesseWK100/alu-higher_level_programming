#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if the character is a lowercase letter
        if ord(char) >= 97 and ord(char) <= 122:  # 'a' to 'z'
            # Convert to uppercase by adjusting ASCII value
            result += chr(ord(char) - 32)
        else:
            result += char  # Non-lowercase characters remain unchanged
    print(result
