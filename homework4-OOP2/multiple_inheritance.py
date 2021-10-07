# Задача 3.
# Реализовать множественное наследование из презентации.
# Надеюсь, я правильно поняла что именно взять из презентации (задачу с мулом)


import re

class Donkey:
    def move(self):
        return 'Donkey Move'
    
    def weight(self):
        return '100 kg'

class Horse:
    def move(self):
        return 'Horse Move'

    def speed(self):
        return '100 miles/h'

class Myl(Donkey, Horse):
    
    def myl_data(self):
        self.horse = re.search(r'\w* ', Horse.move(self)).group()
        self.donkey = re.search(r'\w* ', Donkey.move(self)).group()
        self.myl = 'Myl'
        return f'The speed of a Myl is like a {self.horse} - {Horse.speed(self)}, and it moves like a horse, and its weight is like a {self.donkey} - {Donkey.weight(self)}'

    def myl_height(self):
        return '150 sm'


class Pony(Myl):
    # Пони наследуется от класса, который тоже имеет в себе наследование, и в итоге можно обращаться к методам всх родительскиз классов
    def pony_data(self):
        self.myl = re.search(r'\w* ', Myl.move(self)).group()      
        return f'The weight of a Pony is like a {self.myl} - {Myl.weight(self)}, and it height {Myl.myl_height(self)}'
        

m = Myl()
print(m.myl_data())
p = Pony()
print(p.pony_data())
print(Myl.mro())