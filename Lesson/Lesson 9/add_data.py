import Student2
def add_data():
    a = Student2.student_register()
    f = open('Studen_register.txt', 'w')
    f.write(str(a))
    f.close()


def edit_data():
    pass
# open file (f = open('.txt', 'rw'))
# read file f.read()
