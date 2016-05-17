#!/usr/bin/python3.4

### globalni funkce pouzivane v dalsich funkcich ###
def input_control(type_of_input, question, *args, **kwargs):
    """
    Funkce na automatickou kontrolu vstupu od uživatele.
    type_of_input: typ proměnné, kterou požadujeme. Může být buďto 'i'(pro integer) nebo 's'(pro string)
    question: řetězec s otázkou
    args: minimální a maximální hodnota, kterou může uživatel zadat, pokud je požadovaná odpověď od uživatele celočíselný hodnota.
            V případě typu i je potřeba zadat spodní i horní hranici rozsahu, který se po uživateli požaduje.
            V případě typu s se může(a nemusí) zadat požadovaná délka řetězce.
    kwargs: slouží v případě typu řetězec, kdy zadání od uživatele musí přesně odpovídat zadanému výrazu. Není Key Sensitive.

    Příklady:
        input_control('i', 'Zadej číslo od 1 do 10ti včetně: ', 1, 10)
        input_control('s', 'Zadej řetězec o délce 2 znaků: ', 2)
        input_control('s', 'Zadej libovolný řetězec: ')
        input_control('s', 'Zadej libovolný řetězec: ', key1='kámen', key2='nůžky')
    """
    allowed_types = ['i', 's']
    if type_of_input not in allowed_types:
        print("Chyba volání funkce input_control! Typ požadované typy mohou být pouze \'", allowed_types ,"\' !")
    elif type_of_input == 'i' and len(args)<2:
        print("Chyba volání funkce input_control! U požadovaného typu proměnné integer('i') musí být zadaná spodní i horní hranice rozsahu")
    elif type_of_input == 's' and len(args)>1:
        print("Chyba volání funkce input_control! U požadovaného typu proměnné string('s') může být zadán pouze maximální počet znaků")
    else:
        while True:
            try:
                if type_of_input == 'i':
                    answer = int(input(question))
                else:
                    answer = input(question)
            except ValueError:
                print('zkus to znova, tohle není ani celé číslo: ')
            else:
                if type_of_input == 'i':
                    if answer<args[0] or answer>args[1]:
                        print('Číslo je mimo zadané rozmezí')
                    else:
                        return answer
                if type_of_input == 's':
                    if args:
                        while len(answer) != args[0]:
                            print('Počet znaků v řetězci neodpovídá zadání, řetězec má mít {} znaků'.format(args[0]))
                            answer = input(question)
                        return answer
                    if kwargs:
                        answer_low = answer.lower()
                        for key, value in kwargs.items():
                            kwargs[key] = value.lower()
                        if answer_low not in kwargs.values():
                            print('Slovo neodpovídá zadání, prosím znova.')
                        else:
                            return answer
                    else:
                        return answer
