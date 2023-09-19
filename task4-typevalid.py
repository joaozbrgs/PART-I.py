error='This message should not be displayed, re-run the task'

num1=int(input('Choose a number'))
num2=int(input('Choose another number'))
print(f'the sum of {num1} and {num2} is equal to {num1+num2}')
message1=input('would you like to keep going?')
if message1=='yes' or message1=="y":
    num3=input('type anything')
    print('the type of data you inserted is',type(num3))
    print('your text is alphanumeric:', num3.isalnum())
    print('your text is a number:', num3.isnumeric())    
    print('your text only contain letters:', num3.isalpha())
    print('your text is in upper case:', num3.isupper())
    print('your text is all in lower case:', num3.islower())
    print('your text is capitalized:', num3.istitle())
else:
    print(error)

print('Thank you for participating')

