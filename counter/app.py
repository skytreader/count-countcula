from counter import Counter
from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget


Window.size = (600, 200)

class CounterWidget(Widget):
    red_count = ObjectProperty(None)
    blue_count = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(CounterWidget, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._keydown_handler)
        self.red_counter = Counter()
        self.blue_counter = Counter()

        self.red_count.text = str(self.red_counter.counter)
        self.blue_count.text = str(self.blue_counter.counter)

    def reset(self):
        self.red_counter.reset()
        self.blue_counter.reset()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._keydown_handler)
        self._keyboard = None

    def _keydown_handler(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'k':
            self.blue_counter.incr()
            self.blue_count.text = str(self.blue_counter.counter)
        elif keycode[1] == 'j':
            self.red_counter.incr()
            self.red_count.text = str(self.red_counter.counter)

        return True

class KickCountLabel(Label):
    """
    See http://robertour.com/2015/07/15/kivy-label-or-widget-with-background-color-property/
    """
    bgcolor = ListProperty([1, 1, 1, 1])

class CounterApp(App):
    
    def build(self):
        return CounterWidget()

Factory.register("KickCountLabel", module="KickCountLabel")

if __name__ == "__main__":
    CounterApp().run()
