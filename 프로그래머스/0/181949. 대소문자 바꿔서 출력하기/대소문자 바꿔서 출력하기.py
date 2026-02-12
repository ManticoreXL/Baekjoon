str = input()

for s in str:
    if 65 <= ord(s) <= 90:
        print(chr(ord(s) + 32), end="")
    elif 97 <= ord(s) <= 122:
        print(chr(ord(s) - 32), end="")