"""Memory, puzzle game of number pairs.
Exercises:
1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

counter = 0
revealedCounter = 0
n = 8
car = path('car.gif')
tiles = list([
        "\U0001F600","\U0001F603","\U0001F607",
        "\U0001F605","\U0001F923", "\U0001F643",
        "\U0001F609", "\U0001F970", "\U0001F60D",
        "\U0001F929", "\U0001F618", "\U0001F972",
        "\U0001F60B", "\U0001F61C", "\U0001F92A",
        "\U0001F911", "\U0001F917", "\U0001F92D",
        "\U0001F92B", "\U0001F914", "\U0001F910",
        "\U0001F928", "\U0001F610", "\U0001F611",
        "\U0001F636", "\U0001F612", "\U0001F644",
        "\U0001F62C", "\U0001F62A", "\U0001F924",
        "\U0001F634", "\U0001F637", "\U0001F912",
        ]) * 2
state = {'mark': None}
hide = [True] * (n * n)

def names():
    up()
    goto(-180, 250)
    color('black')
    write('Gerardo Mora Beltran', align = 'left', font = ('arial', 9, 'normal'))
    goto(-180, 230)
    color('black')
    write('Maximiliano Martinez Marquez', align = 'left', font = ('arial', 9, 'normal'))
    goto(-180, 210)
    color('black')
    write('Alejandro Treviño Garcia', align = 'left', font = ('arial', 9, 'normal'))
    down()

def displayCounter():
    up()
    goto(120, 230)
    color('black')
    write("Taps: " + str(counter), align = 'left', font = ('arial', 16, 'normal'))
    down()

def displayWinner():
    up()
    goto(-180, -240)
    color('black')
    write('Ganaste un auto!, Felicidades!', align = 'left', font = ('arial', 12, 'normal'))
    down()
    
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    global n
    return int((x + 200) // 50 + ((y + 200) // 50) * n)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % n) * 50 - 200, (count // n) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global counter
    global revealedCounter
    
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        revealedCounter += 1
    
    counter += 1
    print("Taps: " + str(counter))
    
    if revealedCounter == len(tiles) / 2:
        print("Ganaste un auto!, Felicidades!")
        displayWinner()
        exit()


def draw():
    """Draw image and tiles."""
    global n
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(n * n):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 20, 'normal'))

    update()
    names()
    displayCounter()
    ontimer(draw, 100)


shuffle(tiles)
setup(550, 550, 500, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()