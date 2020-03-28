while True:
    print("please enter your age")
    age=input()
    if age.isdecimal():
        break
    print("enter a number for your age")

while True:
    print("please enter your password")
    password=input()
    if password.isalnum():
        break
    print("passwords can have only letters and numbers")
