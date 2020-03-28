def collatz(number):
    if (number%2==0):
        a=number//2
        print(a)

    elif (number%2==1):
        b= 3*number + 1
        print(b)

collatz(5)
collatz(6)