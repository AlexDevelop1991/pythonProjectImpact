                      #list
array =[]

int_array = [3, 4, 5, 6, 7, 87, 8]
char_array = ['s', 'a', 'l', 'u', 't']
float_array = [5.4, 34.5, 6.2]
bool_array = [True, False, False, True]
#show array
print(int_array)
print(char_array)
print(float_array)
print(bool_array)

#Show array by elements using Index

for i in range(0,6):
    print(int_array[i])

for i in range(0, len(char_array)):
    print(char_array[i])

#Show array by elements using IN

for i in float_array:
    print(i)

#Show array by elements using IN

for i in bool_array:
    print(i)

# _____Read elemets______

#Array declaration
test = []
#Len read
l = int(input("enter the array length: "))  #Задаёшь количество(длинну)

for i in range(0, l):
    test.append(int(input('enter element with index' + str(i) + '/n')))

print(test)

# Array declaration
a =    [1, 1, 2, 5, 8, 13, 22, 34, 35, 2, 3]
#Index: 0  1  2  3  4  5   6    7   8  9  10

#Guest the result
print(a[3]) # 5

print(a[a[3]]) #13
#print (a[a[5]]) #Error



