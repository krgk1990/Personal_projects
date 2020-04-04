# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:04:55 2020

@author: Gokul
"""
import itertools
from colorama import Fore, Back, Style, init
init()

play = True
players = itertools.cycle([1,2])


def game_board(game_temp, player=0,row=0,column=0,display=False):
    try:
        if game_temp[row][column] != 0:
            print("Already taken, please chose another")
            return game_temp, False
        #print("   0  1  2")
        print("   "+"  ".join([str(i) for i in range(len(game_temp))]))
        if not display:
            game_temp[row][column]=player
        for count,row in enumerate(game_temp):
            # print(count,row)
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count,colored_row)
        
        return game_temp, True

    except Exception as e:
        print(e)
        return game_temp, False

def winner(game):

    def same(l):
        if l.count(l[0]) == len(l) and l[0]!=0:
            return True
        else:
            return False

    for row in game:
        if same(row):
            print(f"Player {row[0]} is the winner-- Horizaontal ")
            return True
    
    diags=[]
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if same(diags):
        print(f"Player {diags[0]} is the winner-- Diagonal ")
        return True
    
    diags = []
    for i in range(len(game)):
        diags.append(game[i][i])
    if same(diags):
        print(f"Player {diags[0]} is the winner -- Diagonal")
        return True

    for col in range(len(game)):
        check = []
        
        for row in game:
            check.append(row[col])
            
        if same(check): 
            print(f"Player {check[0]} is the winner -- Vertical")
            return True
    return False
            
while play:
    # game = [[0,0,0],
    #         [0,0,0],
    #         [0,0,0]]
    
    game_size = int(input("Whats the game size of Tic Tac Toe"))

    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game,display=True)  
    
    while not game_won:
        current_player = next(players)
        print(f"current_player: {current_player }")
        
        played = False
        
        while not played:
            col_choice = int(input("What column you want to play? "))
            row_choice = int(input("What Row you want to play? "))
            game, played = game_board(game, current_player, row_choice, col_choice)
            
        if winner(game):
            game_won = True
            again = input("Game over, Would you like to play again (y/n)")
            if again.lower() == 'y':
                print("Restarting....")
            else:
                print("Bye....")
                play = False
