def cell_next_status(board_state, row, column):
    live_neighbour_count = 0
    if row > 0:
        if column > 0:
            if board_state[row-1][column-1] == 1:
                live_neighbour_count += 1
            if board_state[row-1][column] == 1:
                live_neighbour_count += 1
            if board_state[row][column-1] == 1:
                live_neighbour_count += 1
        if column == 0:
            if board_state[row-1][column] == 1:
                live_neighbour_count += 1
        if column < len(board_state[0]) - 1:
            if board_state[row-1][column+1] == 1:
                live_neighbour_count += 1
            if board_state[row][column+1] == 1:
                live_neighbour_count += 1
    if row == 0:
        if column > 0:
            if board_state[row][column-1] == 1:
                live_neighbour_count += 1
        if column < len(board_state[0])-1:
            if board_state[row][column+1] == 1:
                live_neighbour_count += 1
    if row < len(board_state) - 1:
        if column > 0:
            if board_state[row+1][column-1] == 1:
                live_neighbour_count += 1
            if board_state[row+1][column] == 1:
                live_neighbour_count += 1
        if column == 0:
            if board_state[row+1][column] == 1:
                live_neighbour_count += 1
        if column < len(board_state[0]) - 1:
            if board_state[row+1][column+1] == 1:
                live_neighbour_count += 1
            
#    print(f'Neighbour count live = {live_neighbour_count}')

    if board_state[row][column] == 0:
        if live_neighbour_count == 3:
            return 1
        else:
            return 0
    else:
        if live_neighbour_count <= 1:
            return 0
        elif live_neighbour_count > 3:
            return 0
        else:
            return 1

def board_next_state(board_state):
    new_board_state = [[0 for i in range(len(board_state[0]))] for j in range(len(board_state))]
    for i,row in enumerate(board_state):
        for j in range(len(row)):
 #           print(f'i == {i}  j == {j}')
 #           print(f'Current Status == {board_state[i][j]}')
 #           print(f' new status == {cell_next_status(board_state, i, j)}')
            new_board_state[i][j] = cell_next_status(board_state, i, j)
 #   print(board_state)
 #   print(new_board_state)    
    return new_board_state

          
        
