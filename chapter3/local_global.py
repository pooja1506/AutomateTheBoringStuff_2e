def spam():
    eggs = 99
    bacon()
    print(bacon())
    print("Eggs=",eggs)

def bacon():
    ham = 101
    eggs = 0
    return eggs

spam()

# Here only the spam function which is called will give value
# of eggs as it is the only local variable present inside the function