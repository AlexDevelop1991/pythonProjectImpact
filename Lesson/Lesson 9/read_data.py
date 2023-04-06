import  json

def read_file():
    f = open('Studen_register.txt', 'r')
    print(f.read())
    students = f.read()
    print(json.load(f.read(students)))
    f.close()