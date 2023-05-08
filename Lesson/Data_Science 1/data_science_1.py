import pandas as pd

# List of strings
lst = ['Impact', 'Academies', 'and', 'Camps', 'Professional', 'courses']

# Calling DataFrame constructor to list
df = pd.DataFrame(lst)
print(df)
print('------------------->')

# Calling DataFrame constructor on list
df = pd.DataFrame(lst, index=['a', 'b', 'c', 'd', 'e', 'f'], columns=['Names'])
print(df)
print('------------------->')

# List on int
lst2 = [11, 22, 33, 44, 55, 66, 77]

# Calling DataFrame constructor after zipping both lists with columns specified
df = pd.DataFrame(list(zip(lst, lst2)), columns=['Name', 'val'])
print(df)
print('------------------->')

# List of lists
lst3 = [['Ion', 15], ['Mihai', 17], ['Vasile', 16], ['Ana', 16]]
df = pd.DataFrame(lst3, columns=['Name', 'Age'])
print(df)