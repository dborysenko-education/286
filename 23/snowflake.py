import turtle
rays = range(8)
for ray in rays: 
    turtle.forward(100)
    for ray in rays: 
      turtle.forward(30)
      turtle.backward(30)
      turtle.right(45)
    turtle.backward(100)
    turtle.right(45)
