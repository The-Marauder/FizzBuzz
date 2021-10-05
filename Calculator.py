x = int(input('Enter the first number '))
y = int(input('Enter the second number '))
z = input('Enter what kind of operation you want to perform :')
result = 0
if z == '+' :
    result = x+y
    
elif z =='-' :
    result = x-y
    4
elif z =='*' :
    result = x*y
    
elif z =='/' :
    result = x/y
    
elif z == '%' :
    result = x%y
   
else :
    result = 'Please enter a valid operator'

print(result)


