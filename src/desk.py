"""
Класс колоды карт и сомой карты.

"""
from itertools import product
from random import shuffle

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♥', '♠', '♣', '♦']


class Card:
    """
    Класс карты
    Описыват одну карту из колоды
    rank - ранг карты от двойки до туза
    suit - масть карты представлена в виде символа масть
    points - количество очков карты
    picture - текстовое представление карты
    """
    
    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        self.picture = f'{self.rank}{self.suit}'
        self.points = points
    
    def __str__(self):
        return self.picture


class Desk:
    """
    Переремешанная (трижды) при создании колода карт. Из 52 карт.
    """
    
    def __init__(self):
        # переделать на генерацию с
        self.cards: list[Card] = []
        self._generate_deck()
        for _ in range(3):  # перемешать трижды.
            shuffle(self.cards)
    
    def _generate_deck(self):
        # функция product создает список из двух переданных ему
        for suit, rank in product(SUITS, RANKS):
            if rank == 'A':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            c = Card(suit=suit, rank=rank, points=points)
            self.cards.append(c)
    
    def get_card(self):
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)
