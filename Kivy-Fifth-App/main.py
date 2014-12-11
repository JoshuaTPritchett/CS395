#Shows how to use the Kivy-Language for widgets and python
#kivy-language allows a user to quickly create widgets that are re-useable and don't bog
#5 Widgets will now change color at random based on input
from kivy.app import App #sets up the apps interface
from kivy.uix.label import Label #imports a simple button
from kivy.uix.scatter import Scatter #keeps track of all touches on kivy app and make bigger/smaller
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import random

class ScatterTextWidget(BoxLayout):
	#contains all the behavior of program now since kv language#
	
	def change_label_color(self, *args):
		color = [random.random() for i in xrange(3)] + [1]
		label = self.ids['Pritchett_label']
		label.color = color

class TutorialApp(App):
    def build(self):
	return  ScatterTextWidget()



		    			 	
if __name__ == "__main__":
	TutorialApp().run()
