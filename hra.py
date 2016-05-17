#!/usr/bin/python3.4
from glib import input_control
import piskvorky
from ai import pc_turn

user_char = input_control('s', 'Chces x nebo o?', arg1='x', arg2='o')
hardness = input_control('s', 'Jakou obtiznost zvolis? Hard, Medium nebo easy?', w1='hard', w2='medium',w3='easy')
starting_user = piskvorky.starter()
if user_char == 'x':
    pc_char = 'o'
else:
    pc_char = 'x'

turn = 1
game_table_char = '-'
game_table = 20*game_table_char
free_positions = []
for _i in range(len(game_table)):
    free_positions.append(_i)

def piskvorky1d(turn, game_table, user_char, pc_char):
    while not piskvorky.evaluate(game_table, user_char, pc_char, free_positions):
        if starting_user:
            game_table = piskvorky.man_turn(game_table, game_table_char, user_char, free_positions)
            game_table = pc_turn(game_table, game_table_char, pc_char, user_char, free_positions, hardness)
            print('{}. kolo: {} | {}'.format(turn, game_table, game_table.count(pc_char)))
        else:
            game_table = pc_turn(game_table, game_table_char, pc_char, user_char, free_positions, hardness)
            print('{}. kolo: {} | {}'.format(turn, game_table, game_table.count(pc_char)))
            if piskvorky.evaluate(game_table, user_char, pc_char, free_positions):
                break
            game_table = piskvorky.man_turn(game_table, game_table_char, user_char, free_positions)
        turn = turn + 1
    if piskvorky.evaluate(game_table, user_char, pc_char, free_positions) == user_char:
        print('Vyhrals')
    elif piskvorky.evaluate(game_table, user_char, pc_char, free_positions) == pc_char:
        print('Pocitac vyhral')
    else:
        print('Remiza, uz neni kam hrat')

piskvorky1d(turn, game_table, user_char, pc_char)
