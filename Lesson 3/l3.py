print('hello world')
#  this is a comment

# addition
print(2 + 2)

# substraction
print(2 - 1)

# multiplication
print(2 * 3)

# division
print(2 / 4)

# power
print(2 ** 3)

num1 = 1
num2 = 2.4
result_1 = num1 +num2

messange1 = 'hello 1'
messange2 = 'hello 2'

result = messange1 + messange2

print (result)

num3 = int(input( 'your number'))

print(num1 + num3)

name = input('Your name:')


print('Hello' + name)

boolVar1 = True
boolVar2 = False

# logical OR
print(boolVar1 or boolVar2)

# logical AND
print(boolVar1 and boolVar2)

# logical NOT
print(not boolVar1)

float_var = 3.14

# int
print(int(float_var))

# string
print(str(float_var))

# bool
print(bool(float_var))

hour = 10

if  0 and hour < 12:

    print('Good morning')

if hour < 12:

    print('Good morning')
else:
    print('hello')

quit_flag = False
match quit_flag:
    case True:
        print('Quitting')
        exit()
    case False:
        print('System is on')

    case _:
        print('Boolean Value was not passed')

status = 0


class Switch:
    on = 1
    off = 0


match status:
    case Switch.on:
        print('Switch is on')
    case Switch.off:
        print(('Switch is off'))

n = 0

match n:
    case n if n  < 0:
        print('Number is negative')
    case n if n == 0:
        print('Number is zero')
    case n if n > 0:
        print('Number is positive')






