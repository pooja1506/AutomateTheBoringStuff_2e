def collatz(number):

    if (number%2==0):
        a = number//2
        print(a)
        return a

    elif (number%2==1):
        b = 3*number + 1
        print(b)
        return b 

number = int(input("enter a value"))
#print(collatz(5))

while number != 1:
    number = collatz(number)
