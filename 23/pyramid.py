import turtle
levels = range(1,11)
for level in levels: 
  turtle.up()
  turtle.goto(-20*level,-20*level)
  turtle.down()
  for brick in range(level):
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)