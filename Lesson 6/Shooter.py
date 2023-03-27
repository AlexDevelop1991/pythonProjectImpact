#  Обьявление данных
# Initial Values
pers_name = input('Set the name:')
pers_hp = 100
max_pers_hp = 100
armor = 50
nr_hits = 1
# Функция атаки
# Function declaration
def attack(pers_hp, dmg = 5):
    # Calling a global variables
    global armor, nr_hits
    # if we have armor
    if armor - dmg > 0:
        # Decrease armor level
        armor = armor - dmg
    else:
        # Decrease hp level
        pers_hp = pers_hp - dmg
    return pers_hp   #Return the value
# Лечебная функция
def heal(pers_hp, live):
    # Calling a global variable
    global max_pers_hp
    # Condition to not add more HP then max
    if pers_hp + live > max_pers_hp:
        pers_hp = max_pers_hp
    else:
        pers_hp = pers_hp + live
    return  pers_hp  # Return the value


# Call Functions
pers_hp = attack(pers_hp, 40)
print(pers_hp)

pers_hp = heal(pers_hp, 20)
print(pers_hp)

# Бой
# Make a battle
for i in range(1, 100):
    # Stop cycle if hp drop below 0
    if pers_hp > 0:
        pers_hp = attack(pers_hp)
    else:
        break
    print('Live', pers_hp)
    print('Armor', armor)
    print('Hit nr', i)
print('You are dead')

for i in range(1, 100):
    # Stop cycle if hp drop below 0
    if pers_hp > 0:
        nr_hits = nr_hits + 1

        # Make a miss every 3 hits
        if nr_hits % 3 == 0:
            pass
        else:
            pers_hp = attack(pers_hp)
        print('____' + pers_hp + '____')
        print('Live', pers_hp)
        print('Armor', armor)
        print('Hit nr', nr_hits)

    else:
        break
print('You are dead')