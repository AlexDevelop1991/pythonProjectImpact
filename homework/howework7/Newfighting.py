# Global variables
fighters = []
heal_power = 10

class Characters():
    # Data declaring
    Name = ''
    Hp = 0
    Armor = 0
    Power = 0
    def __init__(self, Name, Hp, Armor, Power):
        self.Name = Name
        self.Hp = Hp
        self.Armor = Armor
        self.Power = Power

class Game(Characters):
     # Function to heal fighter
    def heal(self):
        global heal_power
        self.Hp += heal_power
        print(self.Name + 'have', self.Hp, 'Hp left')



        # Function fo attack
    def attacked(self, Damage):
        if self.Hp - Damage > 0:
            self.Hp -= Damage
            print(self.Name + 'have', self.Hp, 'Hp left')
            return True

        else:
            print(self.Name, 'is deadth')
            return False


# Read players number
# Better 2 players
while 1:
    try:
        nr = int(input('How many personage are in game?'))
        break

    except:
        print('Wrong data type')
        continue

# Read data about Fighters
for i in range(0, nr):
    name = input('Name:')
    try:
        Hp = int(input('HP'))
        Armor = int(input('Armor'))
        break
    except:
        fighters.append(Game(name, Hp, Armor, Power))
    continue

    Power = int(input('Power'))

# Declaring Game Data
alive = True
player1 = fighters[0]
player2 = fighters[1]

cur_player = player1
next_player = player2

while alive:

    # User interface
    print('Turn to choose for', cur_player.Name)
    print('Enter 1 for attack other player')
    print('Enter 2 for heall')
    print('Enter 3 to Continue')
    move = int(input())  # Тут добавить try except

    #Game logic
    if move == 1:
        alive = next_player.attacked(cur_player.Power)
    elif move == 2:
        cur_player.heal()
    elif move == 3:
        continue

    # Swith players
    if cur_player == player1:
        cur_player = player2
        next_player = player1
    else:
        cur_player = player1
        next_player = player2


