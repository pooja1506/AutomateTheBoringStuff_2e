#method is used to call on a value
spam = ['hello', 'hi', 'howdy', 'heyas']
a = spam.index('hi')

#append - adds the value at the end of the list
spam.append('hey')
print(spam)

#insert - it can be used to add the value anywhere in the list
spam.insert(1,'hey')
print(spam)

#remove the value from the list
spam.remove('howdy')
print(spam)

#sorting of values
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

#reverse the values of the list
spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam)