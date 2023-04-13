from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Orange'
        return (MDScreen(MDIconButton(icon='language-python', pos_hits={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.8, 0.8))))


Example().run()