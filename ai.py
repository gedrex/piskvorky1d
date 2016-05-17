#!/usr/bin/python3.4
from random import randint, randrange, sample
import piskvorky

def pc_turn(game_table, game_table_char, pc_char, user_char, free_positions, hardness):
    """
    pc_turn(game_table, game_table_char, pc_char, user_char, free_positions, hardness)
    -- pc_turn('hraci pole', 'znk volneho hraciho pole', 'znak hrace - pc', 'znak hrace - cloveka', [volne pozice], obtiznost<'easy', 'medium', 'hard')
    pomoci funkce player_turn
    """
    #retezce, ktere se mohou vyskytovat v poli(game_table) a na ktere pocitac bude reagovat
    defender0 = user_char+game_table_char+user_char
    defender1 = 2*user_char+game_table_char
    defender2 = game_table_char+2*user_char
    defender3 = 3*game_table_char+user_char
    hard_defender3 = 2*game_table_char+user_char
    defender4 = user_char+3*game_table_char
    hard_defender4 = user_char+2*game_table_char
    offender0 = pc_char+game_table_char+pc_char
    offender1 = 2*pc_char+game_table_char
    offender2 = game_table_char+2*pc_char

    #strategie pocitace podle obdiznosti
    def strategy(hardness):
        if offender0 in game_table:
            pc_choice = game_table.index(offender0)+1
        elif offender1 in game_table:
            pc_choice = game_table.index(offender1)+2
        elif offender2 in game_table:
            pc_choice = game_table.index(offender2)
        elif defender0 in game_table:
            pc_choice = game_table.index(defender0)+1
        elif defender1 in game_table:
            pc_choice = game_table.index(defender1)+2
        elif defender2 in game_table:
            pc_choice = game_table.index(defender2)
        elif hardness == 'easy':
            if defender3 in game_table:
                pc_choice = game_table.index(defender3)+randrange(3)
            elif defender4 in game_table:
                pc_choice = game_table.index(defender4)+1+randrange(3)
            else:
                choice = randrange(len(free_positions))
                pc_choice = free_positions[choice]
        elif hardness == 'medium':
            if defender3 in game_table:
                pc_choice = game_table.index(defender3)+randrange(1,3)
            elif defender4 in game_table:
                pc_choice = game_table.index(defender4)+1+randrange(2)
            else:
                choice = randrange(len(free_positions))
                pc_choice = free_positions[choice]
        elif hardness == 'hard':
            if hard_defender3 in game_table:
                pc_choice = game_table.index(defender3)+1
            elif hard_defender4 in game_table:
                pc_choice = game_table.index(defender4)+1
        else:
            #pokud se nevyskytuji dane retezce v hracim poli, vybere PC pseudonahodne z volnych pozic(free_positions)
            pc_choice = randrange(len(free_positions))
        return free_positions[pc_choice]

    pc_choice = strategy(hardness)
    return piskvorky.player_turn(game_table, pc_choice, pc_char, free_positions)
