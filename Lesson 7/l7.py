       # Try, Except
try:
    print(x)
except:
    print('The x is not declared')
#Множество исключений
try:
    print(x)
except NameError:
    print('Variable x is not defined')
except:
    print('Something else went wrong')

    #Try except else
try:
    print('Hello')
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')

    #Try except finally
try:
    print(x)
except:
    print('Something went wrong')
finally:
    print('The "try except" is finished')
