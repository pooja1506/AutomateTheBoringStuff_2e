birthdays = {'Pooja':'June 15','Shakshi':'August 16','Dev':'December 9'}

while True:
    print("Enter a name")
    name=input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is birthday of ' + name)
    else:
        print("name not in birthdays")
        print("enter your birthdate")
        birthdate=input()
        birthdays[name]=birthdate
        print("Birthday database updated")