import webbrowser, sys, pyperclip


#sys.argv #[mapit.py', 'street', 'number', 'city']

#check if command line arguments were passed

if len(sys.argv) > 1:
    #[mapit.py', 'street', 'number', 'city'] -> 'andrianou 24 Athens'
    address = ' '.join(sys.argv[1:]) #we dont want the mapit.py
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/<Address>
webbrowser.open('https://www.google.com/maps/place/' + address)
