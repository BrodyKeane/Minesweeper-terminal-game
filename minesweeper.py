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

                if tile == 0:
                    tile_counters[list][ind] += ' '
                else:
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





#verfies format for moves and calls move maker

def move_verify(length, width, clean_board, visible_board, mine_counters):
    game = 'avtive'
    current_board = clean_board
    visible_tiles = []

    max_width_ind = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
    width_ind = [max_width_ind[char] for char in range(width)]
    length_ind = [str(i) for i in range(length)]

    print('You  make moves in the format "a1" to dig a tile or "a1f" to place a flag')

    while game == 'active':
        move = input('Input your move:  ')

        if len(move) != 2 and len(move) != 3:
            print('invalid format')
            print('You  make moves in the format "a1" to dig a tile or "a1f" to place a flag')
            continue

        if move[0].upper not in width_ind:
            print('invalid format')
            print('First character was not a valid letter')
            continue
        try:
            if int(move[1]) not in length_ind:
                print('invalid format')
                print('Second character was not a valid number')
                continue
        except:
            print('invalid format')
            print('Second character was not a valid number')
            continue

        if len(move) == 3 and move[2] != 'f':
            print('invalid format')
            print('Third charater did not = f')
            continue

        move_ind = width_ind.find(move[0])
        move_ind += int(move[1])

        if len(move) == 2:
            game = mine_checker(move_ind, mine_counters)
            move_feedback = move_dig(current_board, visible_board, mine_counters, move_ind)
            visible_tiles = move_feedback[0]
            current_board = move_feedback[1]
        




#checks if the players move was a mine

def mine_checker(move_ind, mine_counters):
    pass





#takes move from move_verify and finds all adjacent tiles mine mine_counters = to 0

def move_dig(current_board, visible_board, mine_counters, move_ind):

    tile_queue = [move_ind]

    #tracks list of tiles that are visible to player to prevent infinite search for nearby 0 tiles

    visible_tiles = []

    for list in range(len(mine_counter)):
        visible_tiles.append([])
        for counter in mine_counter[list]:
            visible_tiles[list] += 0

    while len(tile_queue) > 0:

        r = tile_queue[0][1]
        c = tile_queue[0][0]
        visible_tiles[r][c] = 1

        current_board[r][c] = visible_board[r][c]

        #checks 4 tile adjacent to first tile in tile_queue for 0 counters and adds 0 counters to tile queue and reveals them to player

        if r - 1 >= 0:
            if visible_tiles[r - 1][c] == 0:
                if mine_counters[r - 1][c] == 0:
                    current_board[r - 1][c] = visible_board[r - 1][c]
                    visible_tiles[r - 1][c] = 1
                    tile_queue.append([r - 1, c])

        if c - 1 >= 0:
            if visible_tiles[r][c - 1] == 0:
                if mine_counters[r][c - 1] == 0:
                    current_board[r][c - 1] = visible_board[r][c - 1]
                    visible_tiles[r][c - 1] = 1
                    tile_queue.append([r, c - 1])

        if c + 1 < len(mine_counters[0]):
            if visible_tiles[r][c + 1] == 0:
                if mine_counters[r][c + 1] == 0:
                    current_board[r][c + 1] = visible_board[r][c + 1]
                    visible_tiles[r][c + 1] = 1
                    tile_queue.append([r, c + 1])

        if r + 1 < len(mine_counters):
            if visible_tiles[r + 1][c] == 0:
                if mine_counters[r + 1][c] == 0:
                    current_board[r + 1][c] = visible_board[r + 1][c]
                    visible_tiles[r + 1][c] = 1
                    tile_queue.append([r + 1, c])

        tile_queue.pop(0)

    return [visible_tiles, current_board]
        











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



# print(num_of_mines)
#print(mine_index)
# print(xboard)
#print(clean_board)
#print(tile_mines)
#print(tile_count)
print(visible_board)
print(mine_counters)