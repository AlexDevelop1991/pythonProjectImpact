f = open('file.txt', 'r')

print(f.read())

print('Only 5')

f = open('file.txt', 'r')

print(f.read(5))

print('Lines:')

print(f.readline())


for x in f:
    print(x)

f.close()

f = open('file2.txt', 'a')

f.write('Now the file has more content!')
f.close()

# Open and read the file after the appending:
f = open('file2.txt', 'r')

print(f.read())

f = open('file2.txt', 'w')
f.write('Woops! I have deleted the content')
f.close()
#Open and read the file after the appending
f = open('file2.txt', 'r')
print(f.read())

#Удаление файла
import os
os.remove('file2.txt')

# Проверка существует ли файл
import os
if os.path.exists('file.txt'):
    os.remove('file.txt')
else:
    print('The file doet not exist')