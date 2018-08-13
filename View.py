from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.clock import Clock
import Data

Builder.load_string('''
<Interface>:
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        pos: 25, 20
        Label:
            canvas.before:
                Color:
                    rgba: 0,0,0,0.5
                Rectangle:
                    pos: self.pos[0], self.pos[1] - 45
                    size: self.size
            size_hint: None, None
            size: 180, 120
            text: 'Your Weather'
        Label:
            id: local_temp
            size_hint: None, None
            size: 180, 210
            text: root.local
            font_size: 60
        Label:
            id: local_name
            size: 180, 300
            size_hint: None, None
            text: root.city
            
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        pos: -25, 20
        
        Label:
            canvas.before:
                Color:
                    rgba: 0,0,0,0.5
                Rectangle:
                    pos: self.pos[0], self.pos[1] - 45
                    size: self.size
            size_hint: None, None
            size: 180, 120
            text: 'Still better than'
        Label:
            id: compare_temp
            size_hint: None, None
            size: 180, 210
            text: root.local
            font_size: 60
        Label:
            id: compare_name
            size: 180, 300
            size_hint: None, None
            text: root.city
            
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        pos: 0, 0
        Label: 
            id: updating
            size: 0, 50
            size_hint: None, None
            text: ''
            
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'center'
        pos: 50, 100
        
        Label:
            canvas.before:
                Color:
                    rgba: 0,0,0,0.5
                Rectangle:
                    pos: self.pos[0], self.pos[1] - 45
                    size: self.size[0] + 50, self.size[1]
            size: 80, 120
            size_hint: None, None
            text: 'Humidity'
        Label:
            id: local_humid
            size_hint: None, None
            size: 225, 120
            text: root.local
            
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'center'
        pos: 50, 80
        Label:
            id: local_heatchill
            size: 52, 120
            size_hint: None, None
            text: 'Heat'
        Label:
            id: local_heat
            size_hint: None, None
            size: 225, 120
            text: root.local
            
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'center'
        pos: -100, 100
        Label:
            canvas.before:
                Color:
                    rgba: 0,0,0,0.5
                Rectangle:
                    pos: self.pos[0], self.pos[1] - 45
                    size: self.size[0] + 50, self.size[1]
            size_hint: None, None
            size: 80, 120
            text: 'Humidity:'
        Label:
            id: compare_humid
            size_hint: None, None
            size: -65, 120
            text: root.city
            
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'center'
        pos: -50, 80
        Label:
            id: compare_heatchill
            size: 212, 120
            size_hint: None, None
            text: 'Heat'
        Label:
            id: compare_heat
            size_hint: None, None
            size: 36, 120
            text: root.local
            
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'bottom'
        
        Button: 
            id: hot_cold
            text: 'Hot'
            on_press: root.switch_temp()
            size: 100, 100
            size_hint: None, None
''')


class Interface(FloatLayout):
    local = city = StringProperty()

    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        self.local = "--"
        self.city = "--"
        self.hot = True

    def update_interface(self):
        self.ids.updating.text = 'Updating...'
        Data.update_weather()
        self.get_local()
        self.get_temp(self.hot)
        self.ids.updating.text = ''

    def get_local(self):
        local = Data.get_city('local')
        self.ids.local_temp.text = str(int(local['main']['temp']))
        self.ids.local_name.text = local['name'] + ", " + local['state']
        self.ids.local_humid.text = str(local['main']['humidity'])
        self.ids.local_heat.text = str(int(local['main']['heat']))

    def get_temp(self, hot):
        if hot is True:
            compare = Data.get_city('hightemp')
            self.ids.compare_heat.text = str(int(compare['main']['heat']))
        else:
            compare = Data.get_city('lowtemp')
            self.ids.compare_heat.text = str(int(compare['main']['chill']))
        self.ids.compare_temp.text = str(int(compare['main']['temp']))
        self.ids.compare_name.text = compare['name'] + ", " + compare['state']
        self.ids.compare_humid.text = str(compare['main']['humidity'])

    def switch_temp(self):
        self.get_temp(not self.hot)
        if self.hot is True:
            self.ids.hot_cold.text = "Cold"
            self.ids.local_heatchill.text = "Chill"
            self.ids.compare_heatchill.text = "Chill"
        else:
            self.ids.hot_cold.text = "Hot"
            self.ids.local_heatchill.text = "Heat"
            self.ids.compare_heatchill.text = "Heat"
        self.hot = not self.hot


class WeatherCompared(App):
    def build(self):
        self.root = root = Interface()
        root.bind(size=self._update_rect)

        with root.canvas.before:
            self.rect = Rectangle(size=root.size)
        return root

    def on_start(self, **kwargs):
        self.root.update_interface()
        Clock.schedule_interval(lambda dt: self.root.update_interface(), 60)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.source = 'Images/Emerald Lake.jpg'


if __name__ == '__main__':
    WeatherCompared().run()
