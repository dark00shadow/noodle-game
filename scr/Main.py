import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *
from RectangleCollision import *

StartMenu = True
Level = 1
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

# Objects

  # Player
PlayerPosX = 300
PlayerPosY = 300
PlayerImage = pyglet.image.load('player--flip=up.png')
PlayerDirection = 'up'
  # Block
if Level == 1:
    Block1PosX = 50
    Block1PosY = 50
if Level == 2:
    Block1PosX = 300
    Block1PosY = 300
Block1Image = pyglet.image.load('block.png')
def Solid(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
    global PlayerDirection, PlayerPosX, PlayerPosY
    if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w-5,obj1h+5,obj2w-5,obj2h-5) and PlayerDirection == 'up': PlayerPosY -= 2
    if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w-5,obj1h+5,obj2w-5,obj2h-5) and PlayerDirection == 'down': PlayerPosY += 2
    if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w-5,obj1h+5,obj2w-5,obj2h-5) and PlayerDirection == 'left': PlayerPosX += 2
    if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w-5,obj1h+5,obj2w-5,obj2h-5) and PlayerDirection == 'right': PlayerPosX -= 2
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
    if StartMenu == False:
        Block1Image.blit(Block1PosX,Block1PosY)
        PlayerImage.blit(PlayerPosX,PlayerPosY)
def update1(dt):
    global StartMenu, PlayerPosX, PlayerPosY, PlayerImage, PlayerDirection, Level
    # StartMenu stuff
    if collision.rectangle(Mousex,MouseY, 230,250, 1,1, 150,100) and StartMenu == True:
        if MouseHandler[mouse.LEFT] and Start.ButtonTriggerOnce == False:
            Start.ButtonTriggerOnce = True
            StartMenu = False
        if not MouseHandler[mouse.LEFT] and Start.ButtonTriggerOnce == True: Start.ButtonTriggerOnce = False
    if StartMenu == False:
        # Player
          # Movment
        if KeyHandler[key.W] and not KeyHandler[key.S] and not KeyHandler[key.A] and not KeyHandler[key.D]:
            PlayerImage = pyglet.image.load('player--flip=up.png')
            PlayerDirection = 'up'
            PlayerPosY += 2
        if KeyHandler[key.S] and not KeyHandler[key.W] and not KeyHandler[key.A] and not KeyHandler[key.D]:
            PlayerImage = pyglet.image.load('player--flip=down.png')
            PlayerDirection = 'down'
            PlayerPosY -= 2
        if KeyHandler[key.A] and not KeyHandler[key.W] and not KeyHandler[key.S] and not KeyHandler[key.D]:
            PlayerImage = pyglet.image.load('player--flip=left.png')
            PlayerDirection = 'left'
            PlayerPosX -= 2
        if KeyHandler[key.D] and not KeyHandler[key.W] and not KeyHandler[key.S] and not KeyHandler[key.A]:
            PlayerImage = pyglet.image.load('player--flip=right.png')
            PlayerDirection = 'right'
            PlayerPosX += 2
          # Solid block
        Solid(PlayerPosX,PlayerPosY, Block1PosX,Block1PosY, 21,7, 32,32)
        if KeyHandler[key.SPACE]:
            Level = 2


pyglet.clock.schedule_interval(update1, 1/120)
pyglet.app.run()