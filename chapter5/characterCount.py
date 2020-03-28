message = "My name is Pooja Mehta , I am 22 years old "
count = {}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
    print(count)
