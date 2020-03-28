spam = {'color': 'red' , 'age':42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in  spam.items():
    print(i)

for k,v in spam.items():
    print('key: ' + k + ' values: ' + str(v))

#get method
print("My favourite is : " + str(spam.get('color','None')) + " color") #none is a fallback value

#set default value
if 'name' not in spam:
    spam['name'] = 'Pooja'
    print(spam)

spam.setdefault('color','black')