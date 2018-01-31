import pyglet
from modules import xboxController

myController = xboxController.XboxController()


window = pyglet.window.Window(resizable=True, caption='DriveRED')
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.text = str(myController.getButton(0))
    label.draw()

@window.event
def mainUpdate(value):
    window.clear()
    label.text = str(myController.getButton(0))
    label.draw()

pyglet.clock.schedule_interval(mainUpdate, 1/120.0)
pyglet.app.run()