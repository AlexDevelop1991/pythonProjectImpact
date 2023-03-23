#Function declaration
def test():
    #Function block
    print('This is test')
#Function call
test()

#Function declaration with parameters
def calc(a, b):
    #Function block
    print(a + b)
    print(a - b)
    print(a * b)
#function call
#Send arguments
calc(3, 4)
calc(5, 8)
calc(3, 4)
calc(4, 9)

#Function declaration
# with initial values
def pr_calc(a, b = 5):
    #Function block
    print(a + b)
    print(a - b)
    print(a * b)

#Function call
#Send arguments
pr_calc(4)
pr_calc(5, 8)

#Function declaration
#Using *args
def arg_calc(*args):
    print(args)
    print(args[0] + args[1])
    print(args[0] * args[1])
    print(args[0] - args[1])
#Functional call
arg_calc(3, 5)

def f_return(word):
    return word.upper()
in_word = input('Write any word')

up_word = f_return(in_word)

print(up_word)

#Print numbers from 1 to 10
for i in range(1, 10):
    print(i)

#Print numbers form 1 to 10 with out 4
for i in range(1, 10):
    if i == 4:
        continue  #cycle stars again
    print(i)

#Print numbers form 1 to 10 until 4
for i in range(1, 10):
    if i == 4:
        break #all cycle stops
    print(i)

#Print numbers form 1 to 10
for i in range(1, 10):
    if i == 4:
        continue
        pass #nothing happen
    print(i)

