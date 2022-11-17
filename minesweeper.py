import random

#Takes user input for board size and verifies that it meets the specified conditions

def size_selector():

    area = []
    length = 0
    width = 0

    while length <= 0 or width <= 0:

        input_size = input('Select a board size in the format: length x width.  Max size = 15 x 25: ')

        length = 0
        width = 0
    
        if ' x ' in input_size:
            area = input_size.split(' x ')
        else:
            continue

        try:    
            length = int(area[0])
            width = int(area[1])
        except:
            continue

        if length > 15 or width > 25:
            length = 0
            continue
    
    area = [int(area[0]), int(area[1])]

    return area





#takes player input for how many mines will be on the board

def mine_amount(area):

    num_of_mines = 0

    decision = input('Would you like to change the number of mines on the board?  ').lower()

    while decision != 'yes' and decision != 'no':
        decision = input('Please input "yes" or "no"  ').lower()

    if decision == 'yes':
        while num_of_mines == 0:
            num = input('How many mines do you want?  ')

            try:    
                num = int(num)
            except:
                continue

            if num > 0 and num < area:
                num_of_mines = num
            else:
                print('Number of mines must be between 0 and {area}'.format(area = area))

    if decision == 'no':
        num_of_mines = round(area * .156)

    return num_of_mines





#takes board size from size_selector and builds the board

def board_builder():

    area = size_selector()
    length = area[0]
    width = area[1]
    board = '\n       '

    width_ind = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
    length_ind = [str(i) for i in range(length)]

    for column in range(width):
        board += '\033[1;37;40m' + width_ind[column] + '       '
    board += '\n   '

    for column in range(width):
        board += '________'

    for row in range(length):
        board += '\n   |'

        for column in range(width):
            board += '       |'
        
        board += '\n' + length_ind[row] + '  |'

        for column in range(width):
            board += '   x   |'

        board += '\n   |'
 
        for column in range(width):
            board += '_______|'

    return [board, area]





#takes xboard and splits it into (length) nested lists containing (width) tiles each.

def tile_tucker(tile_list, length, width):

    tile_index = []
    index_tracker = 0
    
    for list in range(length):
        tile_index.append([])

        for tile in range(width):
            tile_index[list].append(tile_list[index_tracker])
            index_tracker += 1
    
    return tile_index






#takes the number of mines and the area and randomly generates the location for all the mines

def mine_assign(num_of_mines, area):
    mine_index = []

    while len(mine_index) < num_of_mines:
        mine = random.randint(0, area - 1)

        if mine not in mine_index:
            mine_index.append(mine)
    
    mine_index.sort()
    
    return mine_index





#takes mine_index and puts mines in tiles

def mine_merger(xboard, mine_index, length, width):

    tile_index = tile_tucker(xboard, length, width)
    index_tracker = 0

    for list in tile_index:
        for tile in list:

            if index_tracker in mine_index:

                row = index_tracker // width
                ind = index_tracker % width
                tile_index[row][ind] += '\033[1;31;40m' + '*\033[1;37;40m'

            index_tracker += 1
    
    return tile_index





#takes mine ind and adds 1 to the mine counter in its 8 surrounding tiles

def mine_counter(mine_index, length, width):
    mine_count = []
    ind = 0

    for list in range(length):
        mine_count.append([])

        for tile in range(width):
            mine_count[list].append(0)

    for mine in mine_index:

        row = mine // width
        ind = mine % width

            #3 tiles above mine

        if row - 1 >= 0:

            if ind - 1 >= 0:
                mine_count[row - 1][ind - 1] += 1

            mine_count[row - 1][ind] += 1

            if ind + 1 < width:
                mine_count[row - 1][ind + 1] += 1

        #2 tiles beside mine

        if ind - 1 >= 0:
            mine_count[row][ind - 1] += 1

        if ind + 1 < width:
            mine_count[row][ind + 1] += 1

        #3 tiles below mine

        if row + 1 < length:

            if ind - 1 >= 0:
                mine_count[row + 1][ind - 1] += 1

            mine_count[row + 1][ind] += 1

            if ind + 1 < width:
                mine_count[row + 1][ind + 1] += 1

    #changes index of mine to '*'

    for mine in mine_index:

        row = mine // width
        ind = mine % width
        mine_count[row][ind] = '*'

    return mine_count
    
    



#adds color to the numbers in mine_counter

def color_counters(mine_index, length, width):
    mines_count = mine_counter(mine_index, length, width)

    for list in range(len(mines_count)):
        for counter in range(len(mines_count[list])):

            if mines_count[list][counter] == 1:
                mines_count[list][counter] = '\033[1;34;40m' + '1\033[1;37;40m'

            if mines_count[list][counter] == 2:
                mines_count[list][counter] = '\033[1;32;40m' + '2\033[1;37;40m'

            if mines_count[list][counter] == 3:
                mines_count[list][counter] = '\033[1;31;40m' + '3\033[1;37;40m'

            if mines_count[list][counter] == 4:
                mines_count[list][counter] = '\033[1;35;40m' + '4\033[1;37;40m'

            if mines_count[list][counter] == 5:
                mines_count[list][counter] = '\033[1;33;40m' +'5\033[1;37;40m'

            if mines_count[list][counter] == 6:
                mines_count[list][counter] = '\033[1;36;40m' + '6\033[1;37;40m'

            if mines_count[list][counter] == 7:
                mines_count[list][counter] = '\033[1;36;40m' + '7\033[1;37;40m'

            if mines_count[list][counter] == 8:
                mines_count[list][counter] = '\033[1;36;40m' + '8\033[1;37;40m'

    return mines_count





#adds mine counters to tile_mines            
    
def tile_counters(tile_list, mine_index, length, width):
    tile_mines = mine_merger(tile_list, mine_index, length, width)
    mine_count = color_counters(mine_index, length, width)
    tile_counters = tile_mines

    for list in range(len(mine_count)):
        for ind in range(len(mine_count[list])):
            tile = mine_count[list][ind]

            if tile != '*':
                tile_counters[list][ind] += str(tile)

    return tile_counters
                 




#displays full board with all mines and counters visible

def unhide_board(tile_count, width):
    unnested_list = []

    for list in tile_count:
        for tile in list:
            unnested_list += tile

    visible_board = ''.join(unnested_list)
    visible_board += '   |\n   |'

    for column in range(width):
        visible_board += '_______|'

    visible_board += '\n'

    return visible_board





#Logic for making moves

def move_maker(length, width, clean_board, mine_counters, visible_board, tile_count, tile_list):

    game = 'active'
    active_board = clean_board
    active_tiles = tile_space(tile_list, length, width)
    visible_tiles = list_constructor(length, width)

    while True:
        print(active_board)
        move = move_verify(length, width)

        if move[2] == 'dig':
            is_mine = mine_checker(move, mine_counters)

            if is_mine == False:
                visible_tiles = find_visible(move, mine_counters, visible_tiles, length, width)
                active_tiles = board_updater(active_tiles, tile_count, visible_tiles, length, width)
                active_board = active_join(active_tiles, width)
                continue

            if is_mine == True:
                print(visible_board)
                print('game lost')
                break

        elif move[2] == 'flag':

            active_tiles = flag(move, active_tiles)
            active_board = active_join(active_tiles, width)
            continue




            
        
                





def tile_space(tile_list, length, width):

    spaced_list = []
    index_tracker = 0
    
    for list in range(length):
        spaced_list.append([])

        for tile in range(width):
            spaced_list[list].append(tile_list[index_tracker] + ' ')
            index_tracker += 1

    return spaced_list









#constructs a nested list for visible_tiles

def list_constructor(length, width):

    list = []

    for row in range(length):
        list.append([])

        for col in range(width):
            list[row].append(0)

    return list






#verfies format for moves and calls move maker

def move_verify(length, width):
    max_width_lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
    width_lst = [max_width_lst[char] for char in range(width)]
    length_lst = [i for i in range(length)]
    move_ind = []

    print('You make moves in the format "a1" to dig a tile or "a1f" to place a flag')

    while True:
        move = input('Input your move:  ')

#checks if the letter index is in the provided list for the board

        if move[0].upper() not in width_lst:
            print('invalid format')
            print('First index was not a valid letter')
            continue

        elif move[-1] != 'f' and move[-1].isdigit() == False:
            print('invalid format')
            print('Second index was not a valid number')
            continue

#if the move was maked as a flag it checks if it is in the right format

        elif move[-1] == 'f':

            if move[1:-1].isdigit() == False:
                print('invalid format')
                print('Second index was not a valid number')
                continue

            elif int(move[1:-1]) not in length_lst:
                print('invalid format')
                print('Second index was out of range')
                continue

            move_ind.append(width_lst.index(move[0].upper()))
            move_ind.append(int(move[1:-1]))
            move_ind.append('flag')
            break
                
#if the move was a not a flag then it is a dig. checks format for dig

        elif move[1:].isdigit == False:
            print('invalid format')
            print('Second index was not a valid number')
            continue

        elif int(move[1:]) not in length_lst:
            print('invalid format')
            print('Second index was out of range')
            continue

        move_ind.append(width_lst.index(move[0].upper()))
        move_ind.append(int(move[1:]))
        move_ind.append('dig')
        break

    return move_ind





#checks if input square is a mine

def mine_checker(move, mine_counters):

    if mine_counters[move[1]][move[0]] == '*':
        return True
    else:
        return False






#finds all tiles that should be made visible from current move

def find_visible(move, mine_counters, visible_tiles, length, width):
    tile_queue = [[move[1], move[0]]]
    visible_tiles[move[1]][move[0]] += 1

    while len(tile_queue) > 0:

        row = tile_queue[0][0]
        col = tile_queue[0][1]

        if mine_counters[row][col] == 0:

            if row - 1 >= 0:
                if visible_tiles[row-1][col] == 0 and mine_counters[row-1][col] != '*':
                    visible_tiles[row-1][col] += 1

                    if mine_counters[row-1][col] == 0:
                        tile_queue.append([row-1, col])

            if col - 1 >= 0:
                if visible_tiles[row][col-1] == 0 and mine_counters[row][col-1] != '*':
                    visible_tiles[row][col-1] += 1
                    
                    if mine_counters[row][col-1] == 0 and mine_counters != '*':
                        tile_queue.append([row, col-1])

            if col + 1 < width:
                if visible_tiles[row][col+1] == 0 and mine_counters[row][col+1] != '*':
                    visible_tiles[row][col+1] += 1

                    if mine_counters[row][col+1] == 0:
                        tile_queue.append([row, col+1])

            if row + 1 < length:
                if visible_tiles[row+1][col] == 0 and mine_counters[row+1][col] != '*':
                    visible_tiles[row+1][col] += 1

                    if mine_counters[row+1][col] == 0:
                        tile_queue.append([row+1, col])
        
        del tile_queue[0]

    return visible_tiles
        

                




# Updates board using players input

def board_updater(active_tiles, tile_count, visible_tiles, length, width):
    
    for row in range(length):
        for tile in range(width):

            if visible_tiles[row][tile] == 1:
                active_tiles[row][tile] = (tile_count[row][tile])

    return active_tiles

                




#creates a board using all active tiles

def active_join(active_tiles, width):

    active_board = ''

    for row in range(len(active_tiles)):
        for tile in range(len(active_tiles[row])):
            active_board += active_tiles[row][tile]

    active_board += '   |\n   |'

    for column in range(width):
        active_board += '_______|'

    active_board += '\n'

    return active_board






def flag(move, active_tiles):

    active_tiles[move[1]][move[0]] = active_tiles[move[1]][move[0]][:-1] + '\033[1;31;40m' + 'P\033[1;37;40m'

    return active_tiles





def main():

    game = board_builder()

    xboard = game[0]
    length = game[1][0]
    width = game[1][1]
    area = length * width

    tile_list = xboard.split('x')
    clean_board = ' '.join(tile_list)

    num_of_mines = mine_amount(area)
    mine_index = mine_assign(num_of_mines, area)
    mine_counters = mine_counter(mine_index, length, width)

    tile_count = tile_counters(tile_list, mine_index, length, width)
    visible_board = unhide_board(tile_count, width)

    move_maker(length, width, clean_board, mine_counters, visible_board, tile_count, tile_list)


    #print(num_of_mines)
    #print(mine_index)
    #print(xboard)
    #print(clean_board)
    #print(tile_mines)
    #print(tile_count)
    #print(visible_board)
    #print(mine_counters)

main()