import sys

class Player:
    def __init__(self, p, k):
        self.player_health = p
        self.knight_health = k

for line in sys.stdin:
    health_list = [int(i) for i in line.split()]
    #print(health_list)
    if len(health_list) > 1:

        gellyfish = Player(health_list[0], health_list[2])
        flower = Player(health_list[1], health_list[3])
        #print('gelly: %d, %d' % (gellyfish.player_health, gellyfish.knight_health))

        if gellyfish.knight_health >= flower.player_health:
            if gellyfish.player_health >= flower.player_health:
                print('Gellyfish')
            else:
                print('Flower')
        else:
            if gellyfish.knight_health >= flower.knight_health:
                print('Gellyfish')
            else:
                print('Flower')
