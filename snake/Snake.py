"""Snake, classic arcade game.
Gerardo Mora Beltran
Maximiliano Martinez Marquez
Alejandro Treviño Garcia

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

# food inicia en el centro, la snake al lado, y la dirección hacía abajo
food = vector(0, 0)
foodRef = vector(0,0)
snake = [vector(10, 0)]
aim = vector(0, -10)
moveFood = 0
speed = 100

def names():
    up()
    goto(30, 170)
    color('red')
    write('Gerardo Mora Beltran', align = 'left', font = ('arial', 7, 'normal'))
    goto(30, 140)
    color('purple')
    write('Maximiliano Martinez Marquez', align = 'left', font = ('arial', 7, 'normal'))
    goto(30, 110)
    color('blue')
    write('Alejandro Treviño Garcia', align = 'left', font = ('arial', 7, 'normal'))
    down()

def changeSpeed(key):
    global speed
    if key == '1':
        speed -= 10
    else:
        speed += 10
    
    return

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

# funcion move del programa (no de la clase vector)
def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        foodRef.x = food.x
        foodRef.y = food.y
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        if body == head:
            square(body.x, body.y, 9, 'black')
        else:
            square(body.x, body.y, 9, 'green')
    
    global moveFood
    
    if moveFood % 7 == 0:
        while True:
            food.x = foodRef.x + randrange(-1, 1) * 10
            food.y = foodRef.y + randrange(-1, 1) * 10
            
            if food not in snake:
                break
    
    moveFood += 1
    square(food.x, food.y, 9, 'orange')
    names()
    update()
    ontimer(move, speed)


#setup configura la ventana 420 de ancho y 420 de alto, la esquina superior izquierda 370
setup(420, 420, 370, 0)
hideturtle() # esconde la turtle
tracer(False) # esconde el graficado
listen() # activamos el escuchar los eventos del teclado
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(lambda: changeSpeed('1'), '1')
onkey(lambda: changeSpeed('2'), '2')
move()
print(snake)
done() # debe de ser la última instrucción
