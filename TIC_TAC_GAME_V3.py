from random import randint, random
from termcolor import colored

def table():
    print('Table')
    print('  1    2    3 ')
    print('    |    |    ', 'A')
    print('----|----|----')
    print('    |    |    ', 'B')
    print('----|----|----')
    print('    |    |    ', 'C')
    print('\n')


def cpu_table():
    print('Comptuer nomenclature')
    print('  1 |  2 |  3 ')
    print('----|----|----')
    print('  4 |  5 |  6 ')
    print('----|----|----')
    print(' 7  |  8 |  9 ')


"""

winner combinations:

1. A1 + A2 + A3
2. B1 + B2 + B3
3. C1 + C2 + C3
4. A1 + B1 + C1 
5. A1 + B2 + C3 
6. A3 + B3 + C3
7. A1 + B2 + C3
8. A3 + B2 + C1 

"""

# Global variable for assign the moves, it's a dictionary that contains the movements
p_k = {
    'a1': ' ',
    'a2': ' ',
    'a3': ' ',
    'b1': ' ',
    'b2': ' ',
    'b3': ' ',
    'c1': ' ',
    'c2': ' ',
    'c3': ' '
}

win = False

no_movements = False

d = {
    'a1': 'finish',
    'a2': 'finish',
    'a3': 'finish',
    'b1': 'finish',
    'b2': 'finish',
    'b3': 'finish',
    'c1': 'finish',
    'c2': 'finish',
    'c3': 'finish'

}

clear = {
    'a1': ' ',
    'a2': ' ',
    'a3': ' ',
    'b1': ' ',
    'b2': ' ',
    'b3': ' ',
    'c1': ' ',
    'c2': ' ',
    'c3': ' '

}

count_move = 0

is_edges = False
is_corner = False
comb_corner_no_center = False
player_goes_center = False
prob_center = random()
center = False

# All the winner combinations
win_comb = {
    'comb1': ['a1', 'a2', 'a3'],
    'comb2': ['b1', 'b2', 'b3'],
    'comb3': ['c1', 'c2', 'c3'],
    'comb4': ['a1', 'b1', 'c1'],
    'comb5': ['a2', 'b2', 'c2'],
    'comb6': ['a3', 'b3', 'c3'],
    'comb7': ['a1', 'b2', 'c3'],
    'comb8': ['a3', 'b2', 'c1']

}


# Function to select who starts
def who_starts():
    start = False
    while not start:
        print('Hey!...I am CPU...')
        print('Nice to meet you!')
        first_choice = input("\nPlease select 1 or 2\n"
                             "\n\nCPU Starts --> 1\n"
                             "Player starts --> 2\n"
                             "\nWho is going to start...: ")
        if first_choice not in ['1', '2']:
            first_choice = input("\n\nOMG... are you stupid or what?\nSelect 1 or 2! ")
        else:
            start = True
    return int(first_choice)


# Function that asks to the user their move and returns one of the possible movments
def user_in():
    if not win:
        # Parameters
        global p_k, count_move
        choice1 = 'wrong'
        choice2 = 'wrong'
        lst = ['A', 'B', 'C']
        ran = False

        # Select the row
        while choice1.upper() not in lst:
            choice1 = input('Please select a row. Choose between A, B or C:   ').upper()

            if not choice1.isalpha():
                print("Hey, that's not even a letter!")
            elif choice1 in lst:
                pass
            else:
                print("Okei, we are getting closer, but there isn't this row in the table!")

        # Select the column
        while not choice2.isdigit() or not ran:
            choice2 = input('Now you have to select a column! 1, 2 or 3:   ')

            if not choice2.isdigit():
                print("Hey that's not even a number!")

            if choice2.isdigit():
                if int(choice2) not in range(1, 4):
                    print('Wrong!!! out of range')
                    ran = False
                else:
                    ran = True
        final_choice = choice1.lower() + str(choice2)
        count_move += 1
        if p_k[final_choice] == ' ':
            p_k[final_choice] = 'X'
        else:
            print("Invalid movement, there's already a piece there!")
            user_in()


# Function that display the Tic Toc table
def display():

    # Variables
    global p_k
    a = "{0:^3} | {1:^3}|{2:^3}  A".format(p_k['a1'], p_k['a2'], p_k['a3'])
    b = "{0:^3} | {1:^3}|{2:^3}  B".format(p_k['b1'], p_k['b2'], p_k['b3'])
    c = "{0:^3} | {1:^3}|{2:^3}  C".format(p_k['c1'], p_k['c2'], p_k['c3'])
    r = "----|----|----"
    col = "{0:^3}   {1:^3}  {2:^3}".format(1, 2, 3)

    # Display
    print(col)
    print(a)
    print(r)
    print(b)
    print(r)
    print(c)


# Function that checks if there is a player winner combination with more than two pieces
def check_player_win_comb():
    """
    Function that checks all the winner combinations and return the first of that combinations that have more than two
    pieces from the player.
    :return: The combination that has two pieces of the player
    """
    count = 0
    win = []
    for comb in win_comb:
        for el in win_comb[comb]:
            win.append(p_k[el])
            # count += 1

        win = ''.join(win).replace(' ', '')
        count += 1
        if win == 'XX':
            break
        else:
            win = []
    else:
        count = 0
    final_combination = 'comb'+ str(count)
    return final_combination


# Function to check if cpu has a win comb
def check_cpu_win_comb():
    """
    Function that checks all the winner combinations and return the first of that combinations that have more than two
    pieces from the computer.
    :return: combination with two pieces from computer
    """
    count = 0
    win = []
    for comb in win_comb:
        for el in win_comb[comb]:
            win.append(p_k[el])
            # count += 1

        win = ''.join(win).replace(' ', '')
        count += 1
        if win == 'OO':
            break
        else:
            win = []
    else:
        count = 0
    final_combination = 'comb'+ str(count)
    return final_combination


# Function that makes the COU choice
def cpu_choice():
    global p_k, win
    cpu_dic = {
        1: 'a1',
        2: 'a2',
        3: 'a3',
        4: 'b1',
        5: 'b2',
        6: 'b3',
        7: 'c1',
        8: 'c2',
        9: 'c3'
    }
    is_player_win = check_player_win_comb()
    is_cpu_win = check_cpu_win_comb()
    made_movement = False
    first_move = False
    if not win:
        if is_cpu_win != 'comb0':
            for element in win_comb[is_cpu_win]:
                if p_k[element] == ' ':
                    p_k[element] = 'O'
                    made_movement = True
                    win = True
                    print('CPU Win, you loose')
                    # Break, breakes the for loop not the if statement
                else:
                    pass
        if is_player_win != 'comb0' and not win:
            for element in win_comb[is_player_win]:
                if p_k[element] == ' ':
                    p_k[element] = 'O'
                    made_movement = True
                else:
                    pass
        if p_k['b2'] == ' ':
            p_k['b2'] = 'O'
            made_movement = True
            first_move = True
        else:
            corner = 'a1 a3 c1 c3'.split()
            chose = randint(0, 3)
            while not first_move and not made_movement and p_k[corner[chose]] == ' ':
                p_k[corner[chose]] = 'O'
                made_movement = True
                first_move = True
        while not made_movement:
            cpu_cho = cpu_dic[randint(1, 9)]
            while p_k[cpu_cho] != ' ' and not made_movement:
                cpu_cho = cpu_dic[randint(1,9)]
            p_k[cpu_cho] = 'O'
            made_movement = True


def cpu_first():
    global prob_center, center, count_move, is_edges, is_corner, win, comb_corner_no_center, player_goes_center, p_k
    corner = 'a1 a3 c1 c3'.split()
    edge = {
        'b1': ['a3', 'c3'],
        'b3': ['a1', 'c1'],
        'a2': ['c1', 'c3'],
        'c2': ['a1', 'a3']
    }
    diagonals = {
        'diag1': ['a1', 'c3'],
        'diag2': ['c1', 'a3']
    }
    lines = {
        'line1': ['a1', 'b1', 'c1'],
        'line2': ['a1', 'a2', 'a3'],
        'line3': ['a3', 'b3', 'c3'],
        'line4': ['c1', 'c2', 'c3']
    }
    triangle = {
        'tria1': ['c1', 'a2', 'c3'],
        'tria2': ['c3', 'b1', 'a3'],
        'tria3': ['a3', 'c2', 'a1'],
        'tria4': ['a1', 'b2', 'c1']
    }
    edges = [p_k['b1'], p_k['b3'], p_k['a2'], p_k['c2']]

    if prob_center >= 0.5 and count_move == 0:
        p_k['b2'] = 'O'
        center = True
        count_move += 1
    elif prob_center < 0.5 and count_move == 0:
        center = False
        p_k[corner[randint(0, 3)]] = 'O'
        count_move += 1
    else:
        pass

    if count_move == 2 and center:
        if 'X' in edges:
            is_edges = True
            is_corner = False
        else:
            is_corner = True
            is_edges = False
    else:
        pass

    if count_move == 2:
        if p_k['b2'] == ' ':
            comb_corner_no_center = True
            player_goes_center = False
        elif p_k['b2'] == 'X':
            comb_corner_no_center = False
            player_goes_center = True
        else:
            pass # what happens if p_k['b2] == 'O' ??
    else:
        pass
    """
        if count_move == 2:
        if p_k['b2'] == ' ':
            comb_corner_no_center = True
        elif p_k['b2'] == 'X':
            player_goes_center = True
        else:
            pass
    else:
        pass
    """

    if center:
        if is_edges:
            if count_move == 2:
                for key in edge:
                    if p_k[key] == 'X':
                        p_k[edge[key][randint(0,1)]] = 'O'
                        count_move += 1
            elif count_move >= 4:
                cpu_choice()
        elif is_corner:
            if count_move == 2:
                for diag in diagonals:
                    for element in diagonals[diag]:
                        if p_k[element] == 'X':
                            for element in diagonals[diag]:
                                if p_k[element] == ' ':
                                    p_k[element] = 'O'
                                    count_move += 1
                                else:
                                    pass
            if count_move == 4:
                if 'X' in edges:
                    if check_player_win_comb() != 'comb0':
                        for element in win_comb[check_player_win_comb()]:
                            if p_k[element] == ' ':
                                p_k[element] = 'O'
                                count_move +=1

                    else:
                        for line in lines:
                            check = []
                            for element in lines[line]:
                                check.append(p_k[element].replace(' ', ''))
                            check = ''.join(check)
                            if check == 'O':
                                for element in lines[line]:
                                    if element in 'a1 a3 c1 c3'.split() and p_k[element] == ' ':
                                        p_k[element] = 'O'
                                        count_move += 1

                else:
                    cpu_choice()
                    count_move +=1
            else:
                pass

            if count_move >= 6:
                is_player_win = check_player_win_comb()
                is_cpu_win = check_cpu_win_comb()
                if not win:
                    if is_cpu_win != 'comb0':
                        for element in win_comb[is_cpu_win]:
                            if p_k[element] == ' ':
                                p_k[element] = 'O'
                                made_movement = True
                                win = True
                                print('CPU Win, you loose')
                                # Break, breakes the for loop not the if statement
                            else:
                                pass
                    elif is_player_win != 'comb0' and not win:
                        for element in win_comb[is_player_win]:
                            if p_k[element] == ' ':
                                p_k[element] = 'O'
                                made_movement = True
                            else:
                                pass
                    else:
                        cpu_choice()
                    count_move +=1
            else:
                pass
        else:
            pass

    elif not center and comb_corner_no_center: # and p_k['b2'] == ' ':
        # The CPU starts in the corner
        # We can check the triangle operation
        if count_move == 2:
            possible_lines = []
            for line in lines:
                check1 = []
                for element in lines[line]:
                    check1.append(p_k[element].replace(' ', ''))
                check1 = ''.join(check1)
                if check1 == 'O':
                    possible_lines.append(line)
            many_lines = len(possible_lines)-1
            for element in lines[possible_lines[randint(0, many_lines)]]:
                if element in corner and p_k[element] == ' ':
                    p_k[element] = 'O'
                    count_move += 1
        elif count_move == 4:
            possible_lines2 = []
            for line in lines:
                check2 = []
                for element in lines[line]:
                    check2.append(p_k[element].replace(' ', ''))
                check2 = ''.join(check2)
                if check2 == 'O':
                    possible_lines2.append(line)
            many_lines2 = len(possible_lines2)-1
            for element in lines[possible_lines2[randint(0, many_lines2)]]:
                if element in corner and p_k[element] == ' ':
                    p_k[element] = 'O'
                    count_move += 1
        elif count_move >= 6:
            if check_cpu_win_comb() != 'comb0':
                for element in win_comb[check_cpu_win_comb()]:
                    if p_k[element] == ' ':
                        p_k[element] = 'O'
                        count_move += 1
            elif check_player_win_comb() != 'comb0':
                for element in win_comb[check_player_win_comb()]:
                    if p_k[element] == ' ':
                        p_k[element] = 'O'
                        count_move += 1
    elif player_goes_center:
        if count_move == 2:
            for diag in diagonals:
                for element in diagonals[diag]:
                    if p_k[element] == 'O':
                        for element in diagonals[diag]:
                            if p_k[element] == ' ':
                                p_k[element] = 'O'
                                count_move +=1
        elif count_move == 4:
            cor = [p_k['a1'], p_k['a3'], p_k['c1'], p_k['c3']]
            if 'X' in cor:
                for element in corner:
                    if p_k[element] == 'O':
                        for element in corner:
                            if p_k[element] == ' ':
                                p_k[element] = 'O'
                                count_move += 1

            else:
                cpu_choice()
                count_move += 1
        else:
            cpu_choice()
            count_move += 1


# Function to check win and moves combination
def check_win():
    """
    A function that checks all the winner combinations to see if there's a win combination, if there's a win
    combination, changes the win variable to true.
    It also checks all the movements. If all the pieces are in the table, it chanes de win variable to true
    :return: Nothing, it changes the win global variable to True
    """
    global p_k, win, clear, count_move
    if not win:
        for comb in win_comb:
            lst = []
            for element in win_comb[comb]:
                lst.append(p_k[element])
            if lst == ['O']*3 or lst == ['X']*3:
                win = True
                count_move = 0

        lst_movements = []
        string_movements = ''
        for element in p_k.values():
            lst_movements.append(element.replace(' ', ''))
            string_movements = ''.join(lst_movements)
            if len(string_movements) == 9:
                win = True
                no_movements = True
                count_move = 0
                print("\n\n\nIt's a draw")
        else:
            pass



def tic_tac_game():
    while not win:

        display()

        user_in()

        check_win()

        cpu_choice()

        check_win()

        if win:
            display()
        else:
            pass



def starts_cpu():
    global win
    while not win:
        cpu_first()
        display()
        check_win()
        user_in()
        if not win:
            display()
        check_win()
        if win:
            display()
            win = True
        else:
            pass




def play():
    global clear, p_k, win, count_move, prob_center, is_edges, is_corner, comb_corner_no_center, player_goes_center
    rematch = True

    while rematch:

        if who_starts() == 2:
            tic_tac_game()
            want_rematch = input("\n\n\nDo you want the rematch? (Y/N): ")
            while want_rematch.lower() not in ['y', 'n']:
                want_rematch = input("Okei, try to select 'y' for rematch, or 'n' for end the game")
            if want_rematch.lower() == 'n':
                print('\nSe you later!')
                rematch = False
                if count_move != 0:
                    count_move = 0
                is_edges = False
                is_corner = False
                comb_corner_no_center = False
                player_goes_center = False
                break
            elif want_rematch.lower() == 'y':
                win = False
                p_k = {
                    'a1': ' ',
                    'a2': ' ',
                    'a3': ' ',
                    'b1': ' ',
                    'b2': ' ',
                    'b3': ' ',
                    'c1': ' ',
                    'c2': ' ',
                    'c3': ' '
                }
                if count_move != 0:
                    count_move = 0
                is_edges = False
                is_corner = False
                comb_corner_no_center = False
                player_goes_center = False
            else:
                pass


        else:
            starts_cpu()
            want_rematch = input("\n\n\nDo you want the rematch? (Y/N): ")
            while want_rematch.lower() not in ['y', 'n']:
                want_rematch = input("Okei, try to select 'y' for rematch, or 'n' for end the game")
            if want_rematch.lower() == 'n':
                print('\nSe you later!')
                rematch = False
                prob_center = random()
                if count_move != 0:
                    count_move = 0
                is_edges = False
                is_corner = False
                comb_corner_no_center = False
                player_goes_center = False
                break
            else:
                prob_center = random()
                win = False
                p_k = {
                    'a1': ' ',
                    'a2': ' ',
                    'a3': ' ',
                    'b1': ' ',
                    'b2': ' ',
                    'b3': ' ',
                    'c1': ' ',
                    'c2': ' ',
                    'c3': ' '
                }
                if count_move != 0:
                    count_move = 0
                is_edges = False
                is_corner = False
                comb_corner_no_center = False
                player_goes_center = False
                pass


play()



# ####### PROBLEMS
# Start in corner, if instead of block the winner
# combination the user move in another location it doesn't do anything There's a chance to win the CPU, if we start
# with a corner and then the computer goes to the center, then we can follow the technique of the start corner to win
# we can solve it if we make the CPU in this particular case move to an edge instead of a corner


# if we let the CPU start, it wins, we make rematch, there're two pieces in the table


