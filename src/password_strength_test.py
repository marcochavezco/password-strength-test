import re

user_password = str(input("Enter a password: "))

# (?=...) positive lookahead: It asserts that a given pattern can be matched.)
passwordRegex = re.compile(r'''(
    ^(?=.{8,15}$)           # Length
    (?=.*[A-Z])             # Upper
    (?=.*[a-z])             # Lower
    (?=.*[0-9])             # Digit
    (?=.*[!@#$%^&*_-]).*$   # Symbol
    )''', re.VERBOSE)

password = passwordRegex.search(user_password)
if password != None:
    print("Your password is strong")
else:
    print("Your password is not secure")
