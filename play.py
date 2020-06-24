from generator import Nbodies
from time import sleep
from constants import R, wait, no_of_bodies
from vpython import *


scene.caption = """
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.
"""
universe = Nbodies(N = no_of_bodies)
sleep(wait)
while(1):
    rate = R
    def showSphere(evt):
        loc = evt.pos
        universe.add_particle(loc)

    scene.bind('click', showSphere)
    universe.update()