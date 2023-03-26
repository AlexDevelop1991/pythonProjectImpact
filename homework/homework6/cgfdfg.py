pers_name = input('Set the name:')
pers_hp = 100
max_pers_hp = 100
armor = 50
nr_hits = 1


def critical(pers_hp, crit_dmg=15):
    global armor, nr_hits

    if armor - crit_dmg > 0:

        armor = armor - crit_dmg
    else:
        pers_hp = pers_hp - crit_dmg

    return pers_hp


def attack(pers_hp, dmg=5):
    global armor, nr_hits

    if armor - dmg > 0:

        armor = armor - dmg
    else:

        pers_hp = pers_hp - dmg

    return pers_hp


def heal(pers_hp, live):
    global max_pers_hp

    if pers_hp + live > max_pers_hp:
        pers_hp = max_pers_hp

    else:
        pers_hp = pers_hp + live

    return pers_hp

pers_hp == critical(pers_hp, 55)
print(pers_hp)

pers_hp = attack(pers_hp, 40)

print(pers_hp)

pers_hp = heal(pers_hp, 20)

print(pers_hp)