#! python3

import re, pyperclip


#Create a regex for phone numbers
phoneRegex = re.compile(r'''
2\d\d-?\d\d-?\d-?\d\d\d\d
#2XX-xxx-xxxx
#2XXXX-XXXXX
''', re.VERBOSE)

#Create a regex for email
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+    #namepart
@                  #@symbol
[a-zA-Z0-9_.+]+    #domail name

''', re.VERBOSE)

#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from the text                        
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

#Change the way they are shown on the screen
resultP = '\n'.join(extractedPhone) + '\n' 
resultE = '\n'.join(extractedEmail)


print(resultP)
print(resultE)
#print(extractedPhone)
#print(extractedEmail)
