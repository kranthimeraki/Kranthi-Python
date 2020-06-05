print('HI Friends Welcome to Fibonacci series')

a = 0
b = 1
add = 0
i=0

n = int(input('Enter the n value:'))

for i in range(n):
    if (i<n):
        a = b
        b = add
        add = a+b
    print(add)
    

   
