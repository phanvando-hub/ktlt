print("Ho va ten: Phan Van Do")
print("MSSV: 205752020710012")

import turtle, random
colors = ["red","green", "blue",]
painter = turtle. Turtle()
painter.pensize (3)
for i in range(12):
    color = random.choice (colors)
    painter.pencolor (color)
    painter.circle (100)
    painter.right (30)
    painter.left (60)
painter.setposition (0, 0)
