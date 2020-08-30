import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.title('Design in turtle')
s.bgcolor('black')
list=['red','blue','brown','violet','maroon','green','orange','white','purple','yellow']
t.pensize(10)
for i in range(300):
	col=i%10
	t.color(list[col])
	t.forward(i)
	t.left(50)
turtle.done()