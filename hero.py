class SuperHero:
    people='people'
    def __int__(self, name, nickname, superpower, health_points, catchphrase):
        self.name =name
        self.nickname =nickname
        self.superpower =superpower
        self.health_points= health_points
        self.catchphrase =catchphrase

    def nameHero(self):
        print(f'Heros name ist {self.name}')
    def hp(self):
        self.health_points *=2
    def __str__(self):
        return (f'ihr nickname {self.nickname}'
                f'\nseine Macht ist {self.superpower}'
                f'\nihr health_ist {self.health_points}'
                f'\nihr catchphrase ist {self.catchphrase}')
    def __len__(self):
        return len (self.catchphrase)

hero = SuperHero('Hinata', 'Seyo', 'abheben', 2, 'Pass den Ball zu mir!')
hero.nameHero()
hero.hp()
print(hero)
print(len(hero))
