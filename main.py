# main.py

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
from nivesha_backend import get_signals

class NiveshaApp(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False

        self.add_tab("📊 Nifty", get_signals("nifty"))
        self.add_tab("🏦 BankNifty", get_signals("banknifty"))
        self.add_tab("📈 Stocks", get_signals("stocks"))
        self.add_tab("🧠 Options", get_signals("options"))

    def add_tab(self, title, signal_text):
        tab = self.tab_list.create_tab(title)
        tab.content = Label(text=signal_text)
        self.add_widget(tab)

class MainApp(App):
    def build(self):
        return NiveshaApp()

if __name__ == '__main__':
    MainApp().run()
