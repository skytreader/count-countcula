from counter import Counter
from kivy.app import App
from kivy.uix.widget import Widget


class CounterWidget(Widget):
    pass

class CounterApp(App):
    
    def build(self):
        return CounterWidget()


if __name__ == "__main__":
    CounterApp().run()
