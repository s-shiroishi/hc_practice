#クラスとは
class Pokemon:
    name = 'リザードン'
    type1 = 'ほのお'
    type2 = 'ひこう'
    hp = 100

    def attack(self):
        return f'{self.name}の攻撃!'

#コンストラクタ

class Pokemon:
    def __init__(self, name: str, type1: str, type2: str, hp: int, mp: int):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.mp = mp

    def attack(self):
        return f'{self.name}の攻撃!'
    
#継承とポリモーフィズム

class Pikachu(Pokemon):
    def attack(self):
        return 'ピカチュウの10万ボルト!'
    
#クラスの抽象化
from abc import ABC, abstractmethod

class Pokemon(ABC):
    @abstractmethod
    def attack(self):
        pass

#カプセル化

#カプセル化

class Pokemon(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @abstractmethod
    def attack(self):
        pass