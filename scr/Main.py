import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *
from RectangleCollision import *
from random import randint
print('Made with pyglet, RectangleCollision and random')

StartMenu = True
Mousex = 0
MouseY = 0
Point = 0
label = pyglet.text.Label('points:' + str(Point), x=5,y=550,color=(0,128,0,255))
# Window

WINDOW = pyglet.window.Window(caption='noodle-game', width=600, height=600)
WINDOW.set_fullscreen(True)
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
    #BP means block position
class BP():
    Block1PosX = 50
    Block1PosY = 50
    Block2PosX = 82
    Block2PosY = 50
    Block3PosX = 50
    Block3PosY = 500
    Block4PosX = 82
    Block4PosY = 500
    Block5PosX = 488
    Block5PosY = 50
    Block6PosX = 520
    Block6PosY = 50
    Block7PosX = 488
    Block7PosY = 500
    Block8PosX = 520
    Block8PosY = 500
Block1Image = pyglet.image.load('block.png')

  # Ramen
RamenPosX = randint(100,500)
RamenPosY = randint(100,500)
RamenImage = pyglet.image.load('ramen.png')

# Turn object solid
def Solid(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
    global PlayerDirection, PlayerPosX, PlayerPosY, RamenPosX, RamenPosY
    if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w-5,obj1h+5,obj2w-5,obj2h-5) and PlayerDirection == 'up': PlayerPosY -= 2
    if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w-5,obj1h+5,obj2w-5,obj2h-5) and PlayerDirection == 'down': PlayerPosY += 2
    if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w-5,obj1h+5,obj2w-5,obj2h-5) and PlayerDirection == 'left': PlayerPosX += 2
    if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w-5,obj1h+5,obj2w-5,obj2h-5) and PlayerDirection == 'right': PlayerPosX -= 2
    if collision.rectangle(RamenPosX,RamenPosY, obj2x,obj2y, 10,10, obj2w,obj2w):
        RamenPosX = randint(100,500)
        RamenPosY = randint(100,500)
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
        Block1Image.blit(BP.Block1PosX,BP.Block1PosY)
        Block1Image.blit(BP.Block2PosX,BP.Block2PosY)
        Block1Image.blit(BP.Block3PosX,BP.Block3PosY)
        Block1Image.blit(BP.Block4PosX,BP.Block4PosY)
        Block1Image.blit(BP.Block5PosX,BP.Block5PosY)
        Block1Image.blit(BP.Block6PosX,BP.Block6PosY)
        Block1Image.blit(BP.Block7PosX,BP.Block7PosY)
        Block1Image.blit(BP.Block8PosX,BP.Block8PosY)
        label.draw()
        RamenImage.blit(RamenPosX,RamenPosY)
        PlayerImage.blit(PlayerPosX,PlayerPosY)
def update1(dt):
    global StartMenu, PlayerPosX, PlayerPosY, PlayerImage, PlayerDirection, Level, Point, RamenPosX, RamenPosY, label
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
        Solid(PlayerPosX,PlayerPosY, BP.Block1PosX,BP.Block1PosY, 21,7, 32,32)
        Solid(PlayerPosX,PlayerPosY, BP.Block2PosX,BP.Block2PosY, 21,7, 32,32)
        Solid(PlayerPosX,PlayerPosY, BP.Block3PosX,BP.Block3PosY, 21,7, 32,32)
        Solid(PlayerPosX,PlayerPosY, BP.Block4PosX,BP.Block4PosY, 21,7, 32,32)
        Solid(PlayerPosX,PlayerPosY, BP.Block5PosX,BP.Block5PosY, 21,7, 32,32)
        Solid(PlayerPosX,PlayerPosY, BP.Block6PosX,BP.Block6PosY, 21,7, 32,32)
        Solid(PlayerPosX,PlayerPosY, BP.Block7PosX,BP.Block7PosY, 21,7, 32,32)
        Solid(PlayerPosX,PlayerPosY, BP.Block8PosX,BP.Block8PosY, 21,7, 32,32)

          # Ramen
        if collision.rectangle(PlayerPosX,PlayerPosY, RamenPosX,RamenPosY, 21,10, 10,10):
            Point += 1
            label = pyglet.text.Label('points:' + str(Point), x=5,y=550,color=(0,128,0,255))
            RamenPosX = randint(100,500)
            RamenPosY = randint(100,500)

# Clock update and pyglet run thing
pyglet.clock.schedule_interval(update1, 1/120)
pyglet.app.run()