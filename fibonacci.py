print('HI Friends Welcome to Fibonacci series')

a = 0
b = 1
add = 0
i=0

for i in range(101):
    if (i<101):
        a = b
        b = add
        add = a+b
    print(add)
    

   
