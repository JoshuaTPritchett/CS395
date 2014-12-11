#show animation with rectangles

from kivy.base import runTouchApp
from kivy.lang import Builder

from kivy.uix.widget import Widget

from kivy.clock import Clock
from kivy.animation import Animation

from kivy.properties import ListProperty

from kivy.core.window import Window

from random import random

Builder.load_string('''
<Root>:
    ClockRect:
        pos: 300, 300
    AnimRect:
        pos: 500, 300
<ClockRect>:
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
<AnimRect>:
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')

class Root(Widget):
    pass

class ClockRect(Widget):
    	velocity = ListProperty([10,20])
	#Create an update method that will draw animation movement of the rectangles
	
	def __init__(self, **kwargs):
		#call the clock from the internal clock library have respond to the 			main init method
		super(ClockRect, self).__init__(**kwargs)
			
		#have the clock make an interval based on the movements of 			self.update for 1/60 seconds.
		Clock.schedule_interval(self.update, 1/60.)

	def update(self, *args):
		#Create x and y movement
		self.x += self.velocity[0]
		self.y += self.velocity[1]

		#give one of the rectangles the clockwise motion
		if self.x < 0 or (self.x +self.width) > Window.width:
			self.velocity[0] *= -1
		if self.y < 0 or (self.y +self.height) > Window.height:
			self.velocity[1] *= -1


class AnimRect(Widget):
    	#create a random movement for widget based on click movement
	def anim_to_random_pos(self):
		#Before we start our random animation cancel all existing
		Animation.cancel_all(self)

		#Set up x and y's
		random_x = random() * (Window.width - self.width)
		random_y = random() * (Window.height - self.height)
	
		#Animation will handle a majority of the movements will grab random x and y 		points then make sure it last for 4 miliseconds/seconds then 			out_elastic will cause a random trajectory towards the edge and bounce.
		anim = Animation(x=random_x, y=random_y, duration = 4, t = 'out_elastic')

		anim.start(self)

   	#Want to call the anim random when you touch the green rectangle
	def on_touch_down(self, touch):
	#Green rectangle will only move when clicked on
		if self.collide_point(*touch.pos):
			self.anim_to_random_pos()

runTouchApp(Root())
