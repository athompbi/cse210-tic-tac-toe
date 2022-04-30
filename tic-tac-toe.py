# improvement ideas
# add play again
# add draw
# add not being able to play over an already claimed location

# create initial list to form grid
grid_list = [1,2,3,4,5,6,7,8,9]



def print_grid():
    """Print grid using values from grid_list

    Parameter: none (uses global variable grid_list)
    Return: nothing
    """

    # print grid using index numbers from grid_list
    print()
    print(f'{grid_list[0]}|{grid_list[1]}|{grid_list[2]}')
    print('-+-+-')
    print(f'{grid_list[3]}|{grid_list[4]}|{grid_list[5]}')
    print('-+-+-')
    print(f'{grid_list[6]}|{grid_list[7]}|{grid_list[8]}')
    print()


def determine_next_turn(last_turn):
    """Determine whose turn it is based on the last turn.

    Parameter: last_turn ('x' or 'o')
    Return: 'o' if last turn was 'x'
            or 'x' if last turn was 'o'
    """

    if last_turn == 'x':
        return 'o'
    if last_turn == 'o':
        return 'x'


def turn(player):
    """Execute a player's turn by asking which space they want to
    change and then changing that space in the grid_list

    Parameter: player (used to label whose turn it is and change
        the space to that player's symbol)
    Return: nothing (changes are made to global variable grid_list)
    """

    print(f"{player}'s turn:")
    square = int(input('Which space do you want to change? (1-9): '))
    # take the square - 1 to get the index for the space that needs changed
    # and change it to the symbol of the player whose turn it is
    grid_list[square-1] = player



def winning():
    """Determine if any of the winning combinations have been made 
    (player has 3 spaces in a row)
    (1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)

    Parameter: none (checks global variable grid_list)
    Return: 'yes' if any of the combinations conditions are met
        'no' if no combinations are made
    """

    # checks winning combination of spaces 1,2,3
    # 1,2,3

    # if x has all three of these spaces, then x wins
    if grid_list[0] == 'x' and grid_list[1] == 'x' and grid_list[2] == 'x':
        print('x wins')

        # conditions for a win have been met so it returns 'yes' to end the turn loop
        return 'yes'
    
    # if o has all three of these spaces, then o wins
    elif grid_list[0] == 'o' and grid_list[1] == 'o' and grid_list[2] == 'o':
        print('o wins')

        # conditions for a win have been met so it returns 'yes' to end the turn loop
        return 'yes'

    # 4,5,6
    elif grid_list[3] == 'x' and grid_list[4] == 'x' and grid_list[5] == 'x':
        print('x wins')
        return 'yes'
    elif grid_list[3] == 'o' and grid_list[4] == 'o' and grid_list[5] == 'o':
        print('o wins')
        return 'yes'

    # 7,8,9
    elif grid_list[6] == 'x' and grid_list[7] == 'x' and grid_list[8] == 'x':
        print('x wins')
        return 'yes'
    elif grid_list[6] == 'o' and grid_list[7] == 'o' and grid_list[8] == 'o':
        print('o wins')
        return 'yes'

    # 1,4,7
    elif grid_list[0] == 'x' and grid_list[3] == 'x' and grid_list[6] == 'x':
        print('x wins')
        return 'yes'
    elif grid_list[0] == 'o' and grid_list[3] == 'o' and grid_list[6] == 'o':
        print('o wins')
        return 'yes'

    # 2,5,8
    elif grid_list[1] == 'x' and grid_list[4] == 'x' and grid_list[7] == 'x':
        print('x wins')
        return 'yes'
    elif grid_list[1] == 'o' and grid_list[4] == 'o' and grid_list[7] == 'o':
        print('o wins')
        return 'yes'

    # 3,6,9
    elif grid_list[2] == 'x' and grid_list[5] == 'x' and grid_list[8] == 'x':
        print('x wins')
        return 'yes'
    elif grid_list[2] == 'o' and grid_list[5] == 'o' and grid_list[8] == 'o':
        print('o wins')
        return 'yes'

    # 1,5,9
    elif grid_list[0] == 'x' and grid_list[4] == 'x' and grid_list[8] == 'x':
        print('x wins')
        return 'yes'
    elif grid_list[0] == 'o' and grid_list[4] == 'o' and grid_list[8] == 'o':
        print('o wins')
        return 'yes'

    # 3,5,7
    elif grid_list[2] == 'x' and grid_list[4] == 'x' and grid_list[6] == 'x':
        print('x wins')
        return 'yes'
    elif grid_list[2] == 'o' and grid_list[4] == 'o' and grid_list[6] == 'o':
        print('o wins')
        return 'yes'

    # if none of the conditions for win have been met
    # then return no and continue turn loop
    else:
        return 'no'
    

def main():

    # print initial grid to show which spaces are available
    print_grid()

    # determine who is going first
    first_turn = input("Who is going first? (x or o): ")

    # pass the first player to turn so that they can execute their turn
    turn(first_turn)

    # reprint the grid with the updated values
    print_grid()

    # determine next turn passed on who had first turn
    next_turn = determine_next_turn(first_turn)

    # execute next player's turn
    turn(next_turn)

    # reprint the grid with the updated values
    print_grid()

    # set default value for win
    win = 'no'
    # repeat turn cycle until win = yes
    while win == 'no':
        # determine next turn
        next_turn = determine_next_turn(next_turn)
        # execute next turn
        turn(next_turn)
        # print new grid
        print_grid()
        # determine if game is over
        # if game is not over, win still = no
        # and the loop continues
        win = winning()

    # final message for after win complete
    print('Congratulations!')
    print()

main()
