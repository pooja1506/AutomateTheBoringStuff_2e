def collatz(number):

    if (number%2==0):
        a = number//2
        print(a)
        return a

    elif (number%2==1):
        b = 3*number + 1
        print(b)
        return b 
try:

    number = int(input("enter a value"))


    while number != 1:
        number = collatz(number)

except ValueError:
    print("Error:Enter a integer value")

