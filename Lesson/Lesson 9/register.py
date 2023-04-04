from read_data import read_file
from add_data import add_data


option = int(input('Прочесть(1) или добавить(2):'))
match option:
    case 1:
        read_file()
    case 2:
        add_data()


