# Actividad 2. Modificación del juego Paint.
___
## Autores:
___
- Alejandro Treviño García      A00825543
- Gerardo Mora Beltrán          A00827128
- Maximiliano Martínez Márquez  A01251527
## Funciones Agregadas
___
**def names()**
- Escribe los nombres
- Autor: Alejandro Treviño
- Código:
```python
def names():
    up()
    goto(-40, 170)
    color('red')
    write('Gerardo Mora Beltran', align = 'left', font = ('arial', 11, 'normal'))
    goto(-40, 140)
    color('purple')
    write('Maximiliano Martinez Marquez', align = 'left', font = ('arial', 11, 'normal'))
    goto(-40, 110)
    color('blue')
    write('Alejandro Treviño Garcia', align = 'left', font = ('arial', 11, 'normal'))
```
![names](https://i.imgur.com/m3Ov1oM.png)
<br>
**def triangle(start, end)**
- Dibuja un triangulo
- Autor: Gerardo Mora
- Código:
```python
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()
```
![triangle](https://media.giphy.com/media/rSrz7h7IpDUoyisqbe/giphy.gif)
<br>
**def rectangle(start, end)**
- Dibuja un rectangulo
- Autor: Gerardo Mora
- Código:
```python
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        if count % 2 == 0:
            forward(end.x - start.x)
        else:
            forward(end.y - start.y)
        
        left(90)

    end_fill()
```
![rectangle](https://media.giphy.com/media/OO8i2741K7f3pVY35E/giphy.gif)
<br>
**def circle2()**
- Dibuja un círculo
- Autor: Alejandro Treviño
- Código:
```python
def circle2(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    right(90)
    down()
    begin_fill()

    for count in range(360):
        forward((end.x - start.x)/120)
        left(1)

    end_fill()
```
![circle](https://media.giphy.com/media/gHcyQNVWBj21JNksCj/giphy.gif)
<br>
**Onkey**
- Cambia el color
- Autor: Alejandro Treviño
- Código:
```python
onkey(lambda: color('pink'), 'P')
```
![color](https://media.giphy.com/media/UYi9724Q0xhaJh9273/giphy.gif)
