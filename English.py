from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from TelaInicial import TelaInicial
from TelaEstudo import Cumprimentos

class EnglishApp(App):
    def build(self):
        gerenciador = ScreenManager()
        tela1 = TelaInicial(name='tela1')
        tela2 = Cumprimentos(name='tela2')
        gerenciador.add_widget(tela1)
        gerenciador.add_widget(tela2)
        return gerenciador


EnglishApp().run()
