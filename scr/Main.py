import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *
from RectangleCollision import *

StartMenu = True

# Window

WINDOW = pyglet.window.Window(caption='noodle-game', width=600, height=600)
WINDOW.set_location(WINDOW.screen.width//2-WINDOW.width//2, WINDOW.screen.height//2-WINDOW.height//2)
WINDOW.set_icon(pyglet.image.load('ramen.png'))
KeyHandler = key.KeyStateHandler()
MouseHandler = mouse.MouseStateHandler()
WINDOW.push_handlers(KeyHandler)
WINDOW.push_handlers(MouseHandler)
pyglet.gl.glClearColor(0.2,0.2,0.2,1)
gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Start menu

class Start():
    Button_Image = pyglet.image.load('StartButton.png')

@WINDOW.event
def on_draw():
    WINDOW.clear()
    if StartMenu == True: Start.Button_Image.blit(230,250)
def update1(dt):
    pass
pyglet.app.run()