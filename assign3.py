
print('1 for addition. '  '2 for subtraction. '  '3 for multiplication. '
      '4 for division. '  '5 for Exponential. '  '6 for remainder. '  )


a = int(input('Enter the value for arithmetic operaion:'))

b = int(input('Enter the value of first operand:'))
c = int(input('Enter the value of second operand:'))


if( a==1 ):
    addi = b+c
    print('Result of addition:',addi)

if( a==2 ):
    sub = b-c
    print('Result of subtraction:',sub)

if( a==3 ):
    mul = b*c
    print('Result of multiplication:',mul)

if( a==4 ):
    div = b//c
    print('Result of Division:',div)

if( a==5 ):
    expo = b**c
    print('Result of Exponent:',expo)

if( a==6 ):
    remai = b%c
    print('Result of remainder:',remai)
