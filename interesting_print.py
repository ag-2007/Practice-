grid = [['.', '.', 'O', 'O', '.', 'O','O','.','.'],
        ['.', 'O', 'O', 'O', 'O', 'O','O','O','.'],
        ['.', 'O', 'O', 'O', 'O', 'O','O','O','.'],
        ['.', '.', 'O', 'O', 'O', 'O','O','.','.'],
        ['.', '.', '.', 'O', 'O', 'O','.','.','.'],
        ['.', '.', '.', '.', 'O', '.','.','.','.']]

i=0
k=0

for i in range (6):
    for k in range (9):
        print(grid[i][k],end='')
    print()