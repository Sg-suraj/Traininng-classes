#ASSINING TH VARIABLE
a="a"
b="b"
c="c"
d="d"
e="e"
f="f"
g="g"
h="h"
i="i"

#STARTING OF THE GAME
p = [
    [a,b,c],
    [d,e,f],
    [g,h,i]
]
m=str(input("Enter first player name :"))
n=str(input("Enter second player name :"))
for row in p:
    print(row)
print("GAME Tic TAC Toe ")


#FIRST PLAYER TURN
print(m, " turns value: O")
x="0"
p[int(input())][int(input())] = x
for row in p:
    print(row)


#SECOND PLAYER TURN
print(n," turns value: X")
x= "X"
p[int(input())][int(input())] = x
for row in p:
    print(row)

#FIRST PLAYER TURN
print(m, " turns value: O")
x= "0"
p[int(input())][int(input())] = x
for row in p:
    print(row)
if((p[0][0]==p[0][1]==p[0][2]) | (p[1][0]==p[1][1]==p[1][2] ) | (p[2][0]==p[2][1]==p[2][2])
    |(p[0][0]==p[1][0]==p[2][0]) | (p[0][1]==p[1][1]==p[2][1]) |(p[0][2]==p[1][2]==p[2][2])
    |(p[0][0]==p[1][1]==p[2][2]) |(p[0][2]==p[1][1]==p[2][0]) ):
    print(m," won the Game")


#SECOND PLAYER TURN
print(n," turns value: X")
x="X"
p[int(input())][int(input())] = x
for row in p:
    print(row)
if((p[0][0]==p[0][1]==p[0][2]) | (p[1][0]==p[1][1]==p[1][2] ) | (p[2][0]==p[2][1]==p[2][2])
    |(p[0][0]==p[1][0]==p[2][0]) | (p[0][1]==p[1][1]==p[2][1]) |(p[0][2]==p[1][2]==p[2][2])
    |(p[0][0]==p[1][1]==p[2][2]) |(p[0][2]==p[1][1]==p[2][0]) ):
    print(n," won the Game")

#FIRST PLAYER TURN
print(m, " turns value: O")
x= "0"
p[int(input())][int(input())] = x
for row in p:
    print(row)
if((p[0][0]==p[0][1]==p[0][2]) | (p[1][0]==p[1][1]==p[1][2] ) | (p[2][0]==p[2][1]==p[2][2])
    |(p[0][0]==p[1][0]==p[2][0]) | (p[0][1]==p[1][1]==p[2][1]) |(p[0][2]==p[1][2]==p[2][2])
    |(p[0][0]==p[1][1]==p[2][2]) |(p[0][2]==p[1][1]==p[2][0]) ):
    print(m," won the Game")

#SECOND PLAYER TURN
print(n," turns value: X")
x= "X"
p[int(input())][int(input())] = x
for row in p:
    print(row)
if((p[0][0]==p[0][1]==p[0][2]) | (p[1][0]==p[1][1]==p[1][2] ) | (p[2][0]==p[2][1]==p[2][2])
    |(p[0][0]==p[1][0]==p[2][0]) | (p[0][1]==p[1][1]==p[2][1]) |(p[0][2]==p[1][2]==p[2][2])
    |(p[0][0]==p[1][1]==p[2][2]) |(p[0][2]==p[1][1]==p[2][0]) ):
    print(n," won the Game")

#FIRST PLAYER TURN
print(m, " turns value: O")
x="0"
p[int(input())][int(input())] = x
for row in p:
    print(row)
if((p[0][0]==p[0][1]==p[0][2]) | (p[1][0]==p[1][1]==p[1][2] ) | (p[2][0]==p[2][1]==p[2][2])
    |(p[0][0]==p[1][0]==p[2][0]) | (p[0][1]==p[1][1]==p[2][1]) |(p[0][2]==p[1][2]==p[2][2])
    |(p[0][0]==p[1][1]==p[2][2]) |(p[0][2]==p[1][1]==p[2][0]) ):
    print(m," won the Game")

#SECOND PLAYER TURN
print(n," turns value: X")
x="X"
p[int(input())][int(input())] = x
for row in p:
    print(row)
if((p[0][0]==p[0][1]==p[0][2]) | (p[1][0]==p[1][1]==p[1][2] ) | (p[2][0]==p[2][1]==p[2][2])
    |(p[0][0]==p[1][0]==p[2][0]) | (p[0][1]==p[1][1]==p[2][1]) |(p[0][2]==p[1][2]==p[2][2])
    |(p[0][0]==p[1][1]==p[2][2]) |(p[0][2]==p[1][1]==p[2][0]) ):
    print(n," won the Game")


#FIRST PLAYER TURN
print(m, " turns value: O")
x="0"
p[int(input())][int(input())] = x
for row in p:
    print(row)
if((p[0][0]==p[0][1]==p[0][2]) | (p[1][0]==p[1][1]==p[1][2] ) | (p[2][0]==p[2][1]==p[2][2])
    |(p[0][0]==p[1][0]==p[2][0]) | (p[0][1]==p[1][1]==p[2][1]) |(p[0][2]==p[1][2]==p[2][2])
    |(p[0][0]==p[1][1]==p[2][2]) |(p[0][2]==p[1][1]==p[2][0]) ):
    print(m," won the Game")