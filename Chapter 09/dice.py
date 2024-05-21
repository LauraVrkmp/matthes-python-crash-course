from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(number)

die_6 = Die()

print("Die with six sides:")
for i in range(10):
    die_6.roll_die()

die_10 = Die(10)

print("Die with ten sides:")
for i in range(10):
    die_10.roll_die()

die_20 = Die(20)

print("Die with twenty sides:")
for i in range(10):
    die_20.roll_die()