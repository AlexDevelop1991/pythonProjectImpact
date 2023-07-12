import re

txt = 'The rain is Spain'
x = re.search('^The.*Spain$', txt)
if x:
    print('Yes! We have a match!')
else:
    print('No match')
