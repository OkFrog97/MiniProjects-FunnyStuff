class Player:
    def blast (self, enemy):
        print ('Shoot in this green face!')
        enemy.die()

class Alien:
    def die(self):
        print ('UUUrrgggh...')

def main ():
    print ('Fight whith Alian')
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input ('Press Enter to escape battlefild')

main ()