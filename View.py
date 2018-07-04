from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from Data import get_local_temp


class Interface(FloatLayout):
    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        self.your_temp = get_local_temp()
        self.your_location = 'Plainfield, IN'
        self.add_widget(Label(
            text='Your Weather',
            size_hint=(.2,1.75),
            text_size=self.size,
            halign='left',
            valign='top'
        ))
        self.add_widget(Label(
            text=str(self.your_temp),
            size_hint=(.2, 1.70),
            text_size=self.size,
            font_size=60,
            halign='left',
            valign='top'
        ))
        self.add_widget(Label(
            text=self.your_location,
            size_hint=(.2, 1.5),
            text_size=self.size,
            halign='left',
            valign='top'
        ))


class WeatherCompared(App):
    def build(self):
        self.root = root = Interface()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0.2, 0.2, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    WeatherCompared().run()
