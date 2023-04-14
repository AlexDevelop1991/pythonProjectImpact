from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from livymd.uix.button import MDReactangleFlatButton
# Creating Demo Class(base class)
class Demo(MDApp):
    def build(self):
        screen = Screen()
        # Defiining label with all the parameters
        self.l = MDLabel(text='HI PEOPLE!', halign='center', text_color=(0.5, 0, 0.5, 1), font_style='Caption')
        # Defining Text field with all the parameters
        self.n = MDTextField(text='Enter name', pos_hint={'center_x': 0.5, 'center_y': 0.8}, size_hint_x=None, width=100)
        # Defining Button with all the parameters
        btn = MDReactangleFlatButton(text='Submit', pos_hint={'center_x': 0.5, 'center_y': 0.3}, on_release= self.btnfunc)
        # Adding widgets to screen
        screen.add_widget(self.n)
        screen.add_widget(btn)
        screen.add_widget(self.l)
        # Returning the screen
        return screen
    # Defining a btnfun() for the button to
    # Call when clicked on it
    def btnfunc(self, obj):
        self.l.text = self.n.text
        print('button is pressed!!')
if __name__ == '__main__':
    Demo().run()