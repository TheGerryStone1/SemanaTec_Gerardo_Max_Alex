# Actividad 3. Modificación del juego Snake.
___
## Autores:
___
- Alejandro Treviño García A00825543
- Gerardo Mora Beltran A00827128
- Maximiliano Martinez Marquez A01251527

## Variables Agregadas
```python
foodRef = vector(0,0)
colorList = ['green', 'blue', 'orange', 'purple', 'pink', 'black', 'grey', 'yellow', 'lime', 'teal']
snakeColor = choice(colorList)
colorList.remove(snakeColor)
headColor = choice(colorList)
colorList.remove(headColor)
foodColor = choice(colorList)
colorList.remove(foodColor)
moveFood = 0
speed = 100
```
## Funciones Agregadas o Modificadas
**def move()**
1. Hace mover la comida un paso a la vez
2. Valida que la comida no esté dentro del snake
3. Cambia los colores del snake y la comida cada que se inicia el juego 
- Autores: Gerardo Mora (1,2), Maximiliano Martinez (3)
- Código:
```python
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
    
    # Aparece snake y comida de distintos colores - Max
    for body in snake:
        if body == head:
            square(body.x, body.y, 9, headColor)
        else:
            square(body.x, body.y, 9, snakeColor)
    
    global moveFood
    
    # Mover comida - Gerardo
    if moveFood % 10 == 0:
        while True:
            foodRandomizer = choice([1, 2, 3, 4])
            
            if foodRandomizer == 1:
                food.x = foodRef.x
                food.y = foodRef.y + 10
                
            elif foodRandomizer == 2:
                food.x = foodRef.x
                food.y = foodRef.y - 10
                
            elif foodRandomizer == 3:
                food.x = foodRef.x + 10
                food.y = foodRef.y
                
            else:
                food.x = foodRef.x - 10
                food.y = foodRef.y
            
            foodRef.x = food.x
            foodRef.y = food.y
            
            if food not in snake:
                break
    
    moveFood += 1
    square(food.x, food.y, 9, foodColor)
    names()
    update()
    ontimer(move, speed)
```
**def names()**
- Escribe los nombres
- Autor: Gerardo Mora
- Código:
```python
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
```
![snake](https://i.makeagif.com/media/5-11-2022/U2dOw4.gif)

