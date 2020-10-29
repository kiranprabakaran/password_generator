import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()+.,[]"

while True:
    password_len = int(input("How many characters do you need in your password?  "))
    password_count = int(input("how many passwords do you need?  "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is/are your passwords ", password)

    print('')

