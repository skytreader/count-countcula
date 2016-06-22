from counter import Counter
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget


Window.size = (600, 200)

class CounterWidget(Widget):
    pass

class CounterApp(App):
    
    def build(self):
        return CounterWidget()


if __name__ == "__main__":
    CounterApp().run()
