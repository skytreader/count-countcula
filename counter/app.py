from counter import Counter
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget


Window.size = (600, 200)

class CounterWidget(Widget):
    
    def __init__(self, **kwargs):
        super(CounterWidget, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._keydown_handler)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._keydown_handler)
        self._keyboard = None

    def _keydown_handler(self, keyboard, keycode, text, modifiers):
        pass

class CounterApp(App):
    
    def build(self):
        return CounterWidget()


if __name__ == "__main__":
    CounterApp().run()
