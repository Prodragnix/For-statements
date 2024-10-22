string=input('Please enter your string:  ')
x=('')
for i in string:
    x=i+x
print('The original string is: '+string)
print('The reversed string is: '+x)