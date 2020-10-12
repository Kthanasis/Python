import pprint
message='This is the text we will use as an example. We can use any text, no matter the size!'
count={}

for character in message.upper(): #we car remove .upper() so it can distinct between
                                  #Uppercase and Lowercase
    count.setdefault(character,0) #this helps to avoid exceptions when a letter does not exist
                                  #sets a default value when a value does not exist
    count[character]=count[character] + 1

pprint.pprint(count)

#if we want to keep the count
print()
tempsave = pprint.pformat(count)
print(tempsave) #if we want to keep the count 
