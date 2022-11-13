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





#takes board size from size_selector and builds the board

def board_builder():

    area = size_selector()
    length = area[0]
    width = area[1]
    board = '_'
    

    for column in range(width):
        board += '________'

    for row in range(length):
        board += '\n|'

        for column in range(width):
            board += '       |'
        
        board += '\n|'

        for column in range(width):
            board += '   x   |'

        board += '\n|'
 
        for column in range(width):
            board += '_______|'

    return [board, area]





#takes the number of mines and the area and randomly generates the location for all the mines

def mine_assign(num_of_mines, area):
    mine_index = []

    while len(mine_index) < num_of_mines:
        mine = random.randint(0, area - 1)

        if mine not in mine_index:
            mine_index.append(mine)
    
    mine_index.sort()
    
    return mine_index

    





game = board_builder()

xboard = game[0]
length = game[1][0]
width = game[1][1]
area = length * width

tiles = xboard.split('x')
clean_board = ' '.join(tiles)

num_of_mines = round(length * width * .156)
mine_index = mine_assign(num_of_mines, area)






print(num_of_mines)
print(mine_index)
print(xboard)
print(clean_board)