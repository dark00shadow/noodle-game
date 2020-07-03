import pyglet
from pyglet.window import mouse, key
from RectangleCollision import *

StartMenu = True

# Start menu

class Start():
    Button_Image = pyglet.image.load('StartButton.png')


# Window

WINDOW = pyglet.window.Window(caption='noodle-game', width=600, height=600)
KeyHandler = key.KeyStateHandler()
MouseHandler = mouse.MouseStateHandler()
WINDOW.push_handlers(KeyHandler)
WINDOW.push_handlers(MouseHandler)