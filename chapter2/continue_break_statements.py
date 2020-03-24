while True:
    print("who are you?")
    name = input()
    if name != 'Joe':
        continue
    print("hello joe , please enter your password")
    password = input()
    if password == 'Seasword':
        break
    print("access granted")



    #continue statement is used to jump back to the start of the loop to re-evaluate the input until its true
    #break statement is used to immediately exit the while loop clause