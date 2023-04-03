import mymodule

mymodule.greeting('Alex')

a = mymodule.person1['age']
print(a)

import mymodule as mm

mm.greeting('Alex')
a = mm.person1['age']
print(a)

from mymodule import person1

print(person1['age'])