#!/usr/bin/python3.4
from random import randint, randrange, sample
from glib import input_control
from ai import pc_turn

def starter():
    """
    starter(None) - losuje nahodne ze 3 cisel. Pokud ho uzivatel uhadne, vraci True, pokud ne, vraci False.
    """
    random_number = randrange(1,4)
    user_choice = input_control('i', 'Počítač vylosoval náhodně číslo od 1 do 3. Když ho uhodneš, hraješ první. \n Tvoje volba?: ', 1,3)
    if user_choice == random_number:
        print('Uhodls, začínáš!')
        return True
    else:
        print('Začíná počítač.')
        return False

def evaluate(game_table, user_char, pc_char, free_positions):
    """
    evaluate(game_table, user_char, pc_char, free_positions)
    vyhodnocuje, zda existuje vitez. Vraci True, pokud existuje vitez(3 znaky v rade) -> vraci znak vitezneho hrace, nebo pokud uz nejsou volna pole -> vraci '!'. Jinak vraci False

    game_table = retezec herniho pole
    user_char = znak hrace
    pc_char = znak pocitace
    free_positions=[volna pole]
    """
    if (user_char*3) in game_table:
        return user_char
    elif (pc_char*3) in game_table:
        return pc_char
    elif len(free_positions) < 1:
        return '!'
    else:
        return False

def player_turn(game_table, played_number, player_char, free_positions):
    """
    player_turn(game_table, played_number, player_char, free_positions)
    Meni pismenka v hracim poli dle tahu hrace nebo pocitace turn('herni pole', cislo zvolene hracem -> int,'hracuv znak', [volna pole] )
    """
    #vymaze z volnych poli prave zahranou pozici
    del free_positions[free_positions.index(played_number)]
    played_number = played_number + 1
    if played_number < 1:
        return player_char + game_table[0:]
    else:
        return game_table[:played_number-1] + player_char + game_table[played_number:]

def man_turn(game_table, game_table_char, user_char, free_positions):
    """
    man_turn(game_table, game_table_char, user_char, free_positions)
    -- man_turn('hraci pole', 'znk volneho hraciho pole', 'znak hrace - cloveka', [volne pozice])
    pomoci funkce player_turn vrati hraci pole se zaznamenanym tahem lidskeho hrace
    """
    while True:
        try:
            user_number = int(input('Hraj číslo od 20: '))-1
        except ValueError:
            print('Hraj číslo od 20, které tam ještě není: ')
        else:
            if user_number not in free_positions:
                print('Číslo je mimo zadané rozmezí nebo uz tam neco je')
            else:
                return player_turn(game_table, user_number, user_char, free_positions)
