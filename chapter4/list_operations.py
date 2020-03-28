spam = ['elepant','monkey','tiger','giraffe','dog']
print(spam)
print(spam[1])
print(spam[2])

print('Hello,' + spam[0])

print(spam[-2])  #negative indexing

print(spam[2:4])  #slicing

print(spam[:3])  #It automatically starts from zero

print(spam[1:]) #It considers till the end of the list

print(len(spam)) #Prints length of the list

#Replacing the values

spam[1]= 'cat' #Replaced monkey with the cat
print(spam)

spam[3]=spam[2]
print(spam)

#concatenation and replication

a = [1,2,3] + ['A','B','C']  #concatenation
print(a)

b = ['X','Y','Z']*3   #replication
print(b)

