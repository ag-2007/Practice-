tictactoe=[[0,0,0],
           [0,0,0],
           [0,0,0]]

print(tictactoe)
for x in range (2):
    ply_1=input("Player 1, Enter your row and column cordinates in the form a b : ")
    list1 = ply_1.strip().split()
    tictactoe[int(list1[0])-1][int(list1[1])-1] = "X"
    print(tictactoe)

    ply_2=input("Player 2, Enter your row and column cordinates in the form a b : ")
    list2 = ply_2.strip().split()
    tictactoe[int(list2[0])-1][int(list2[1])-1] = "O"
    print(tictactoe)

ply_1=input("Enter your row and column cordinates in the form a b : ")
list1 = ply_1.strip().split()
tictactoe[int(list1[0])-1][int(list1[1])-1] = "X"
print(tictactoe)



