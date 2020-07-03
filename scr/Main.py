import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *
from RectangleCollision import *

StartMenu = True
Mousex = 0
MouseY = 0
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
    ButtonImage = pyglet.image.load('StartButton.png')
    ButtonTriggerOnce = False
# Other
@WINDOW.event
def on_mouse_motion(x,y,dx,dy):
    global Mousex, MouseY
    Mousex = x
    MouseY = y
@WINDOW.event
def on_draw():
    WINDOW.clear()
    if StartMenu == True: Start.ButtonImage.blit(230,250)
def update1(dt):
    global StartMenu
    if collision.rectangle(Mousex,MouseY, 230,250, 1,1, 150,100) and StartMenu == True:
        if MouseHandler[mouse.LEFT] and Start.ButtonTriggerOnce == False:
            Start.ButtonTriggerOnce = True
            StartMenu = False
        if not MouseHandler[mouse.LEFT] and Start.ButtonTriggerOnce == True: Start.ButtonTriggerOnce = False
pyglet.clock.schedule_interval(update1, 1/120)
pyglet.app.run()