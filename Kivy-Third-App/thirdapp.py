



from kivy.app import App #sets up the apps interface

from kivy.uix.label import Label #imports a simple button
from kivy.uix.scatter import Scatter #keeps track of all touches on kivy app and make bigger/smaller
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class TutorialApp(App):
    def build(self): #when app runs calls build and what ever build returns calls widget chosen
	b = BoxLayout()
	t= TextInput(font_size = 80)

	
	f = FloatLayout()
	s = Scatter()
	l = Label(text= "Hello!",
	          font_size = 100)
	#Add the Scatter output that allows for moving and resizing to the float layout
	f.add_widget(s)
	#Add the Label for hello! to the scatter that will allow for movement/ resizing
	s.add_widget(l)

	#Make the box layout the root widget and add the float layout and newly created Text 		input
	b.add_widget(f)
	b.add_widget(t)
	return b #return b which is a box layout widget that will be the highest priority widget
		    			 	
if __name__ == "__main__":
	TutorialApp().run()
