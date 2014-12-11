from kivy.app import App #sets up the apps interface

from kivy.uix.label import Label #imports a simple button
from kivy.uix.scatter import Scatter #keeps track of all touches on kivy app and make bigger/smaller
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class TutorialApp(App):
    def build(self): #when app runs calls build and what ever build returns calls widget chosen
	b = BoxLayout(orientation = 'vertical') #changes the orientation set to vertical rather 						than horizontal base
	t= TextInput(font_size = 80,
		     size_hint_y=None,  
		     height = 200,
		     text = 'default')#even with specific size it will size the 						 text porportionally

	l = Label(text= 'default',
	          font_size = 100)
	#Add the Scatter output that allows for moving and resizing to the float layout


	t.bind(text=l.setter('text')) #setter automatically sets a text for the 				     function that automatically sets the text for 				             the label. This will cause our label to update 				             based on input text

	f = FloatLayout()
	s = Scatter()

	f.add_widget(s)
	#Add the Label for hello! to the scatter that will allow for movement/ resizing
	s.add_widget(l)

	#Make the box layout the root widget and add the float layout and newly created Text 		input
	b.add_widget(t)
	b.add_widget(f)
	return b #return b which is a box layout widget that will be the highest priority widget



		    			 	
if __name__ == "__main__":
	TutorialApp().run()
