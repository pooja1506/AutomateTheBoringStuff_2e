import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search("My numer is 256-444-9876")
print("Phone number found: " + mo.group())

#Regex helps to find the regular patterns

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search("My numer is 256-444-9876")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

print(mo.groups())
area_code,phone = mo.groups()
print(area_code)
print(phone)

#matching multiple groups with a pipe
heroRegex = re.compile(r'batman|Tina')
hero = heroRegex.search('batman and Tina')
print(hero.group())

#optional matching with question mark

batRegex = re.compile(r'bat(wo)?man')
bat=batRegex.search("she is a batwoman")
print(bat.group())


#matching zero or more with a star
batRegex1 = re.compile(r'bat(wo)*man')
bat1=batRegex1.search("she is a batwowoman")
print(bat1.group())

#matching one or more with a star
batRegex2 = re.compile(r'bat(wo)+man')
bat2=batRegex2.search("she is a batwowowoman")
print(bat2.group())

#matching repetitions with braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

#greedy - prints max possible values , non greedy - prints the least possible
greedyhaRegex1 = re.compile(r'(Ha){3,5}')
mo2=greedyhaRegex1.search('HaHaHaHaHa')
print(mo2.group())

#find all - finds all the possible matches in the statement
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo3=phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo3)

#wildcard character - will match any number of characters
atRegex = re.compile(r'.at')
mo5 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo5)

#case sensitive matching
robocop = re.compile(r'robocop', re.I)
mo6=robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo6)