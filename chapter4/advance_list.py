supplies = ['pens','staplers','flamethrowers','binders']
for i in range(len(supplies)):
    print('The index is ' + str(i) + ' for: ' + supplies[i])

# in and not in operators
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')


#solving the for loop using enumerate function
#Enumerate is used when you need both index and the item name

supplies = ['pens','staplers','flamethrowers','binders']
for index , item in enumerate(supplies):
    print('The index is ' + str(index) + ' for: ' + item)