name = 'Pooja'
age = 24
print("Hello my name is ," + name + " and i am " + str(age) + " years old.")

#using %s to call variables.
print("Hello my name is %s. I am %s years old" %(name,age))

#using f-string to call variables
print(f"Hello my name is {name}. I am {age} years old")

# upper , lower , isupper , islower
name = name.upper()
print(name)

name=name.lower()
print(name)

a = 'Hello'.isupper()  #checks whether hello is all upper case or not
print(a)

b = 'HELLO'.isupper()
print(b)