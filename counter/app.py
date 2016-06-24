from counter import Counter
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
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

class CounterApp(App):
    
    def build(self):
        return CounterWidget()


if __name__ == "__main__":
    CounterApp().run()
