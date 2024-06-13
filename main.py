from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50]
        self.spacing = 10

        # Adicionando um rótulo
        self.add_widget(Label(text="L O G I N", font_size=24))

        # Adicionando campos de entrada de texto

        self.name_input = TextInput(hint_text='Email', multiline=False)
        self.add_widget(self.name_input)

        self.password_input = TextInput(hint_text='Senha', multiline=False, password=True)
        self.add_widget(self.password_input)

        # Botões
        self.login_button = Button(text='Login', size_hint=(None, None), size=(200, 50))
        self.login_button.bind(on_press=self.on_login)
        self.add_widget(self.login_button)

        self.cadastro_button = Button(text='Cadastro', size_hint=(None, None), size=(200, 50))
        self.cadastro_button.bind(on_press=self.on_cadastro)
        self.add_widget(self.cadastro_button)

    def on_login(self, *args):
        self.parent.parent.current = 'Cadastro'
    
    def on_cadastro(self, *args):
        self.parent.parent.current = 'Cadastro'


class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 50]
        self.spacing = 10

        # Adicionando um rótulo
        self.add_widget(Label(text=" .:: C A D A S T R O ::.", font_size=24))

        # Adicionando campos de entrada de texto

        # Email
        self.add_widget(Label(text="Email", font_size=18))
        self.email_input = TextInput(hint_text='Digite aqui...', multiline=False)
        self.add_widget(self.email_input)

        # Senha
        self.add_widget(Label(text="Senha", font_size=18))
        self.password_input = TextInput(hint_text='Digite aqui...', multiline=False, password=True)
        self.add_widget(self.password_input)

        # Adicionando botão de cadastro
        self.cadastrar_button = Button(text='Cadastrar', size_hint=(None, None), size=(200, 50))
        self.cadastrar_button.bind(on_press=self.on_cadastrar)
        self.add_widget(self.cadastrar_button)

    def on_cadastrar(self, instance):
        # Adicione a lógica de cadastro aqui
        print("Cadastro button pressed")


class MyApp(App):
    def build(self):
        Window.size = (300, 500)
        sm = ScreenManager()
        tela_login = TelaLogin()
        tela_cadastro = TelaCadastro()

        screen_login = Screen(name='Login')
        screen_cadastro = Screen(name='Cadastro')

        screen_login.add_widget(tela_login)
        screen_cadastro.add_widget(tela_cadastro)

        sm.add_widget(screen_login)
        sm.add_widget(screen_cadastro)

        return sm


if __name__ == '__main__':
    MyApp().run()
