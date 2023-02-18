"""
Класс игры
интерфейс оконный и прочие
https://pythobyte.com/build-a-blackjack-command-line-game-3o4b-30c75f63/
Пример через руки с подробным описанием для консоли
http://pythonicway.com/python-games/python-textgames/15-python-black-jack
так же для консоли, немного описание, но вроде со вполне рабочими идеями.
"""
import tkinter as graph
import tkinter.messagebox as mb

from src.desk import *
from src.player import Hand


class Game:
    def __init__(self):
        self.win = None
        self.label_dealer_text = None
        self.label_user_text = None
        self.label_desk_text = None
        self.label_result_text = None
        self.button_get = None
        self.button_pas = None
        
        self.player = Hand("Player")
        self.dealer = Hand("Dealer")
        self.desk: Desk = Desk()
    
    def _init_window(self):
        self.win = graph.Tk()
        self.win.geometry("300x140")
        self.win.title('Игра в Black Jack')
        self.win.resizable(False, False)
        # кнопки
        self.button_get = graph.Button(self.win, width='15', text='Взять карту', command=self.button_get_click)
        self.button_get.place(x=10, y=60)
        self.button_pas = graph.Button(self.win, width='15', text='Довольно...', command=self.button_pas_click)
        self.button_pas.place(x=170, y=60)
        # # метки, надписи.
        self.label_desk_text = graph.Label(self.win, text='Игра начата, ход дилера', fg="red")
        self.label_desk_text.place(x=10, y=0)
        self.label_user_text = graph.Label(self.win, text='У игрока: ', fg="black")
        self.label_user_text.place(x=10, y=30)
        self.label_dealer_text = graph.Label(self.win, text='У дилера: ', fg="black")
        self.label_dealer_text.place(x=10, y=100)
    
    def start_game(self):
        print("до mainloop")
        
        self.dealer.ask_card(self.desk)
        
        self.player.ask_card(self.desk)
        self.player.ask_card(self.desk)
        # настройка окна
        self._init_window()
        # вынести в метод
        self.update_label_text(self.label_user_text, self.player)
        self.update_label_text(self.label_dealer_text, self.dealer)
        self.win.mainloop()
        print("после mainloop")
    
    def update_label_text(self, label: graph.Label, player: Hand):
        hand_cards = []
        for card in player.cards:
            hand_cards.append(str(card))
        label['text'] = f'у {player.name} {"".join(hand_cards)} :{player.points}'
    
    def button_get_click(self):
        self.player.ask_card(self.desk)
        if self.player.points > 21:
            self.label_user_text["fg"] = "red"
            self.button_get['state'] = graph.DISABLED
            self.end_game()
        self.update_label_text(self.label_user_text, self.player)
    
    def end_game(self):
        pass
    
    def button_pas_click(self):
        while self.dealer.points < 16:
            self.dealer.ask_card(self.desk)
            self.update_label_text(self.label_dealer_text, self.dealer)
        if 21 >= self.dealer.points > self.player.points:
            self.label_desk_text["text"] = 'Победил дилер.'
