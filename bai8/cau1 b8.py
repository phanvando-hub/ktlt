print('Ho va ten: Phan Van Do')
print('MSSV:205752020710012')

import turtle
window = turtle.Screen()
window.bgcolor('lightgreen')
painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pensize(3)
def drawsq(t, s):
    for i in ranger(4):
        t.forward(s)
        t.left(90)
for i in range(1,180):
        painter.left(90)
        drawsq(painter, 200)
