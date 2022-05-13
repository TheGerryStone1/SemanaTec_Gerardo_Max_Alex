# Actividad de Competencia. Modificación del juego Memorama.
___
## Autores:
___
- Alejandro Treviño García A00825543
- Gerardo Mora Beltran A00827128
- Maximiliano Martinez Marquez A01251527

## Variables Agregadas
```python
counter = 0
revealedCounter = 0
n = 8
```

## Funciones Agregadas o Modificadas
**def name()**
- Escribe los nombres
- Autor: Gerardo Mora
- Código:
```python
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
```
**def displayCounter()**
- Despliega el contador de taps en la pantalla del juego
- Autor: Alejandro Treviño
- Código:
```python
def displayCounter():
    up()
    goto(120, 230)
    color('black')
    write("Taps: " + str(counter), align = 'left', font = ('arial', 16, 'normal'))
    down()
```
**def displayWinner()**
- Muestra el mensaje al haber ganado el juego
- Autor: Alejandro Treviño
- Código:
```python
def displayWinner():
    up()
    goto(-180, -240)
    color('black')
    write('Ganaste un auto!, Felicidades!', align = 'left', font = ('arial', 12, 'normal'))
    down()
```
**def tap()**
- Se implementa el contador de taps y detecta cuando todos los cuadros se han destapado (manda a llamar a la función DisplayWinner())
- Autor: Gerardo Mora
- Código:
```python
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
```
**Emojis**
- Se muestran emojis en las casillas en vez de dígitos
- Autor: Maximiliano Martínez
- Código:
```python
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
        "\U0001F634", "\U0001F637",
        ]) * 2
```
![memorama](https://media.giphy.com/media/wxPNT2AJDcZ7mbRChH/giphy.gif)
___

**Link de Videos**
- Gerardo Mora:
- Maximiliano Martínez: https://youtu.be/ykcISVGinz8
- Alejandro Treviño: https://youtu.be/kR9ICiDWp1Y
