a = "Hello world".startswith("Hello")
print(a)

b = "Hello world".endswith("world")
print(b)

#join
c='Abc'.join(['my','name','is','simon'])
print(c)

#split
d= 'MyABCnameABCisABCSimon'.split('ABC')
print(d)

#partitioning for strings
e= "Hello,world!!".partition('w')
print(e)

# ljust , rjust , center
f = "hello".rjust(5)
print(f)

g="hello".ljust(5)
print(g)

h="hello".center(10,"=")
print(h)

#removing white space using strip , lstrip , rstrip
spam = " Hello,world   "
i=spam.strip()
print(i)

j=spam.rstrip()
print(j)

k=spam.lstrip()
print(k)

#get numeric values of character

l=ord('A')
print(l)

m=chr(65)
print(m)