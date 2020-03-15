from game.subsystems.entities import *


class Shop:

    def __init__ (self, inital_money=300):
        self.bank = inital_money

    def buy(self, tower: Tower):
        self.bank -= tower.price

    def makeMoney(self, enemy: Enemy):
        self.bank += enemy.money

class Player:
    def __init__ (self, initial_health=50):
        self.health = initial_health
        self.dead = False

    def hit(self, enemy:Enemy):
        self.health -= enemy.originalHealth
        if self.health <= 0:
            self.game_over()

    def game_over(self):
        self.dead = True