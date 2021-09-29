x = 0 
while x<= 100 : 
    x = x+1
    if x%15 == 0 : 
        print('Fizzbuzz')
    elif x%3 == 0 : 
        print('Fizz')
    elif x%5 == 0 : 
        print('Buzz')
    else :
        print(x)
