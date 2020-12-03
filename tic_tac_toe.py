a=[[" "," "," "],[" "," "," "],[" "," "," "]]
p1=input("Choise of Player1 ")
p2=input("Choise of Player2 ")
p="draw"
print("Enter the positions as in a matrix")
print("Enter the row and column only seperated by a space")
print("The positioning starts from (1,1)")
print("If some position contains 'x' or 'o' it can't be rewritten")
print("Enter any position if you don't have any empty position to enter, but it wont replace it")
while 1:
    b=[int(i) for i in input("Player1 enter the position ").split(" ")]
    if a[b[0]-1][b[1]-1]==" ":
        a[b[0]-1][b[1]-1]=p1
    c=[int(i) for i in input("Player2 enter the position ").split(" ")]
    if a[c[0]-1][c[1]-1]==" ":
        a[c[0]-1][c[1]-1]=p2
    for i in a:
        for j in i:
            print(j,end=" ")
        print()
    for i in a:
        if i==['x','x','x']:
            p="player1"
            break
        elif i==['o','o','o']:
            p="player2"
            break
    for i in range(3):
        c=0
        d=0
        for j in range(3):
            if a[j][i]==p1:
                c+=1
                if c==3:
                    p='player1'
                    break
            elif a[j][i]==p2:
                d+=1
                if d==3:
                    p="player2"
                    break
    if (a[0][0]==a[1][1] and a[1][1]==a[2][2]) or (a[0][2]==a[1][1] and a[1][1]==a[2][0]):
        if a[1][1]==p1:
            p="player1"
        elif a[1][1]==p2:
            p="player2"              
    if p!="draw":
        print("winner is",p)
        break
    g=0
    for i in a:
        for j in i:
            if j!=" ":
                g+=1
    if g==9:
        print(p)
        break