a = 'hello'.isalpha() #True only if inside the inverted comma there are only alphabets
print(a)

b = 'hello123'.isalnum() #True only if it has both alphabets and numbers
print(b)

c = '1506'.isdecimal() #True if only numeric values present
print(c)

d = '   '.isspace() #True if there are spaces
print(d)

e = 'This Is Life'.istitle()  #True only if first letter of every word is upper case and others be lower
print(e)