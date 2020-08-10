import turtle
t=turtle.Pen()
turtle.bgcolor("sandy brown")
colours=["red","orange","yellow","green","white","pink","blue","gold","turquoise","purple","brown","violet"]
sides=12
t.speed(0)
for a in range(1000):
	t.pencolor(colours[ a % sides])
	t.forward(1*a)
	t.left(360/sides +1)
	t.width(3)

input()