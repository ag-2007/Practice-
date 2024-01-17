import numpy

game = [
    [2, 2, 1],
    [2, 1, 1],
    [1, 2, 1]
]

def line_match(game):
    matches = []
    for i in range(3):
        set_r = set(game[i])
        if len(set_r) == 1 and game[i][0] != 0:
            matches.append(game[i][0])
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        return -1
    else:
        return 0

def column(game):
    matches = []
    trans = numpy.transpose(game)
    for i in range(3):
        set_c = set(trans[i])
        if len(set_c) == 1 and trans[i][0] != 0:
            matches.append(list(set_c)[0])
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        return -1
    else:
        return 0

def diagonal_match(game):
    matches = []
    if game[1][1] != 0:
        if game[1][1] == game[0][0] == game[2][2]:
            matches.append(game[1][1])
        if game[1][1] == game[0][2] == game[2][0]:
            matches.append(game[1][1])
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        return -1
    else:
        return 0

row_winner = line_match(game)
column_winner = line_match(numpy.transpose(game))
diagonal_winner = diagonal_match(game)

if row_winner > 0:
    print(str(row_winner) + " row wins!")
elif row_winner == -1:
    print("Incorrect tic-tac-toe, please share relevant tic-tac-toe inputs")

if column_winner > 0:
    print(str(column_winner) + " column wins!")
elif column_winner == -1:
    print("Incorrect tic-tac-toe, please share relevant tic-tac-toe inputs")

if diagonal_winner > 0:
    print(str(diagonal_winner) + " diagonal wins!")
elif diagonal_winner == -1:
    print("Incorrect tic-tac-toe, please share relevant tic-tac-toe inputs")
