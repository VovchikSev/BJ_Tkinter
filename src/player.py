"""
Класс игроков
"""
from src.desk import *


class Hand:
    def __init__(self, name: str):
        self.name = name
        self.cards = []
        self.points = 0
    
    def ask_card(self, desk: Desk):
        card: Card = desk.get_card()
        self.points += card.points
        self.cards.append(card)
    
    def __str__(self):
        return
