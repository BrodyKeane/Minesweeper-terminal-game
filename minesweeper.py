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
    board = '''_'''

    for column in range(width):
        board += '________'

    for row in range(length):

        for segment in range(2):
            board += '''
|'''
        
            for column in range(width):
                    board += '       |'
    
        board += '''
|'''
        
        for column in range(width):
            board += '_______|'

    return [board, area]


    
#first int position:
# 2(8 * width + 1) + 5
    

# board[2(8 * width + 1) + 5] = 'x'
#Figur out how to modify specific squares in board
#maybe split all 'squares'(center cegment of square) into different strings
#then re-append with new value between
#binary bomb values should be stored seperatly for every square in a list
#list indexes should corrospond to board position
#nested lists for each row?


# def tile_finder(length, width):
#     tile_index = []
#     current_index = 2 * (8 * width + 1)

#     for row in range(length):
#         current_index += 5
#         tile_index += current_index

#         for collumn in range(width - 1):
#             current_index += 8
#             tile_index += current_index
        
#         current_index += 2 * (8 * width + 1) + 9

#     return tile_index
        
    



game = board_builder()

board = game[0]
length = game[1][0]
width = game[1][1]

tile_index = tile_finder(length, width)


for ind in tile_index:
    print(ind)

for ind in tile_index:
    print(board[ind])





print(board)
