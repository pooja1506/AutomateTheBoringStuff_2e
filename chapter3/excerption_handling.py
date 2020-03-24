def spam(divideBy):
    return 42/divideBy

try:
    print(spam(12))
    print(spam(5))
    print(spam(0))
    print(spam(7))

except ZeroDivisionError:
    print("Invalid arguement")