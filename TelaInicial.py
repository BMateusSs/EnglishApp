from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical',
                           pos_hint={'center_x': 0.5, 'center_y': 1})

        botão1 = Button(text='Greetings',
                        size_hint=(None, None),
                        size=(100, 40),
                        pos_hint={'center_x': 0.5, 'y': 0.9})

        botão2 = Button(text='Conhencendo',
                        size_hint=(None, None),
                        size=(100, 40),
                        pos_hint={'center_x': 0.5, 'y': 0.5})

        botão3 = Button(text='Cores',
                        size_hint=(None, None),
                        size=(100, 40),
                        pos_hint={'center_x': 0.5, 'y': 0.5})

        botão1.bind(on_press=self.mudar_tela)
        botão2.bind(on_press=self.mudar_tela)
        botão3.bind(on_press=self.mudar_tela)

        layout.add_widget(botão1)
        layout.add_widget(botão2)
        layout.add_widget(botão3)

        self.add_widget(layout)

    def mudar_tela(self, button):
        if button.text == "Greetings":
            modulo = 0
        elif button.text == "Conhencendo":
            modulo = 1
        elif button.text == "Cores":
            modulo = 2
        self.manager.current = 'tela2'
        self.manager.get_screen("tela2").alterar_tarefa(modulo)
