class Creature:
    def __init__(self, name, attack, defence):
           self.name = name
           self.attack = attack
           self.defence = defence

    def __str__(self):
        return f'{self.name}, ({self.attack}/{self.defence})' 

class CreatureModifier:
    def __init__(self, creature:Creature):
        self.creature = creature
        self.next_modifier:Creature = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class DoubleAttack(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}\'s attack.')
        self.creature.attack *= 2
        super().handle()

class DoubleDefence(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}\'s defence.')
        self.creature.defence *= 2
        super().handle()

if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)

    root.add_modifier(DoubleAttack(goblin))
    root.add_modifier(DoubleDefence(goblin))

    root.handle()
    print(goblin)