import pyglet
from modules import xboxController

myController = xboxController.XboxController()


window = pyglet.window.Window(resizable=True, caption='DriveRED')

leftLabel = pyglet.text.Label("HI",
                          font_name='Times New Roman',
                          font_size=36,
                          x=10, y=50)

rightLabel = pyglet.text.Label("HI",
                          font_name='Times New Roman',
                          font_size=36,
                          x=10, y=10)


def toPercent(value):
    return str(round(value * 100)) + "%"

#@window.event
#def on_draw():

@window.event
def mainUpdate(value):
    window.clear()

    leftTread = myController.getAxis(1)
    rightTread = myController.getAxis(3)

    leftLabel.text = "Left Power: " + toPercent(leftTread)
    leftLabel.draw()

    rightLabel.text = "Right Power: " + toPercent(rightTread)
    rightLabel.draw()

pyglet.clock.schedule_interval(mainUpdate, 1/60.0)
pyglet.app.run()