



from kivy.app import App #sets up the apps interface

from kivy.uix.label import Label #imports a simple button
from kivy.uix.scatter import Scatter #keeps track of all touches on kivy app and make bigger/smaller
from kivy.uix.floatlayout import FloatLayout


class TutorialApp(App):
    def build(self): #when app runs calls build and what ever build returns calls widget chosen
	f = FloatLayout()
	s = Scatter()
	l = Label(text= "Hello!",
	          font_size = 100)
	
	f.add_widget(s)
	s.add_widget(l)
	return f
		    			 	
if __name__ == "__main__":
	TutorialApp().run()
