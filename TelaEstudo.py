from PopUp import MeuPopUp
from kivy.clock import Clock
from Atividades import Greetings, Conhecendo, Cores
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from TelaInicial import TelaInicial


class Cumprimentos(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.i = 0
        self.pontos = 0
        self.layout2 = BoxLayout(orientation='vertical',
                                 pos_hint={'center_x': 0.5, 'center_y': 0.7})

        self.tarefas = None

        self.layoute = BoxLayout(orientation='vertical',
                                 pos_hint={'x': 0, 'center_y': 0.9})

        self.layoutP = BoxLayout(orientation='vertical',
                                 pos_hint={'x': 0, 'center_y': 0.7})

        self.layoutT = BoxLayout(orientation='vertical',
                                 pos_hint={'x': 0, 'center_y': 0.6})

        self.layoutPontos = BoxLayout(orientation='vertical',
                                      pos_hint={'center_x': -0.4, 'center_y': 0.9})

        self.exibir_pontos = Label(text=f"Pontos: 0",
                                   font_size=25,
                                   pos_hint={"x": 0.5, "center_y": 0.8})

        self.exibir_pergunta = Label(text=" ",
                                     color=(0, 1, 0, 1),
                                     font_size=30,
                                     pos_hint={'x': 0, 'center_y': 0.5})

        self.exibir_enuciado = Label(text='Traduza essa expressão',
                                     font_size=25,
                                     pos_hint={'x': 0., 'y': 0.9})

        self.exibir_tradução = Label(text="",
                                     color=(0, 1, 1, 1),
                                     font_size=30,
                                     pos_hint={'x': 0, 'center_y': 0.5})

        self.expressoes = [Greetings, Conhecendo, Cores]

        self.add_widget(self.layout2)
        self.add_widget(self.layoute)
        self.add_widget(self.layoutP)
        self.add_widget(self.layoutT)
        self.add_widget(self.layoutPontos)

    def alterar_tarefa(self, modulo):
        self.tarefas = self.expressoes[modulo]
        self.modulo1()

    def modulo1(self):
        self.layout2.clear_widgets()
        self.layoute.clear_widgets()
        self.layoutP.clear_widgets()
        self.layoutT.clear_widgets()
        self.layoutPontos.clear_widgets()

        self.qp = list(self.tarefas.keys())

        if self.i >= len(self.qp):
            Clock.schedule_once(lambda dt: self.mensagem_final())
            return

        pergunta = list(self.tarefas.keys())[self.i]
        self.c = self.i + 1
        print(f"QPerguntas: {len(self.qp)}")
        self.exibir_pergunta.text = pergunta

        print(pergunta)
        self.resposta = self.tarefas[pergunta]['resposta_correta']

        if "tradução" in self.tarefas[pergunta]:
            self.exibir_tradução.text = self.tarefas[pergunta]["tradução"]
            self.layoutT.add_widget(self.exibir_tradução)

        enuciado = self.tarefas[pergunta]["enuciado"]

        self.exibir_enuciado.text = enuciado

        for a in self.tarefas[pergunta]['alternativas']:
            alternativas = Button(text=a,
                                  size_hint=(None, None),
                                  size=(180, 40),
                                  pos_hint={'center_x': 0.5, 'y': 2})

            alternativas.bind(on_press=self.acertou)
            self.layout2.add_widget(alternativas)

        self.layoutPontos.add_widget(self.exibir_pontos)
        self.layoutP.add_widget(self.exibir_pergunta)
        self.layoute.add_widget(self.exibir_enuciado)

    def acertou(self, instance):
        if instance.text == self.resposta:
            self.exibir_enuciado.text = 'Você acertou!'
            print(self.i)
            self.pontos += 5
            self.exibir_pontos.text = f"Pontos: {self.pontos}"
            self.i += 1

            Clock.schedule_once(lambda dt: self.modulo1(), 2)

    def mensagem_final(self):
        self.layoute.clear_widgets()
        mensagem = Label(text="Você respondeu todas as perguntas!",
                         pos_hint={"center_x": 0.5, "center_y": 0},
                         font_size=30)
        self.layoute.add_widget(mensagem)
        Clock.schedule_once(lambda dt: self.retornar(), 2)

    def retornar(self):
        self.manager.current = "tela1"
