tuple_ex = ('Hola', 5, 'Test', 4.55, False)

#tuple_ex.append #Error

print(tuple_ex[0])

print(tuple_ex + ('New', 'data', 1))

                       #___Set___
#Declaration of simple array
simple_array = [1, 2, 3, 4, 5, 0, 2, 3, 4, 5, 2, 3]

#Declaration of set
set_array2 = {4, 3, 2, 4, 5, 5, 41, 2}

#Convert to set
set_array = set(simple_array)

print(simple_array)
print(set_array)
print(set_array2)

                  #Dictionares
dictionar = {'Key': 'Value', 'Int': 3, 'Float': 23.4, 'Bool': True}

print(dictionar.get('Key'))

dictionar.update({'int': 4})

dictionar['Key'] = 'New Value'

print(dictionar)
