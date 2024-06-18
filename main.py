from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import sp
from kivy.config import Config
import requests
import json

link = "https://teste-48527-default-rtdb.firebaseio.com/"

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '610')
Config.write()

kv_code = """
<LoginScreen>:
    orientation: 'vertical'
    padding: 20
    spacing: 20

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: sp(400)
        spacing: 20
        pos_hint: {'center_y': 0.7}

        Image:
            source: '/Users/Educação/Downloads/icon_perfil.png'
            size_hint_y: None
            height: sp(100)
            keep_ratio: True
            allow_stretch: True

        Label:
            text: 'Login'
            color: (0.98, 0.56, 0.65, 1) 
            font_size: sp(24)
            size_hint_y: None
            height: sp(40)
            bold: True

        BoxLayout:
            size_hint_y: None
            height: sp(40)
            spacing: 10

            Label:
                text: 'Email:'
                size_hint_x: None
                width: sp(100)
                color: (0.98, 0.56, 0.65, 1)
                font_size: sp(18)
            TextInput:
                id: email
                multiline: False
                background_color: (1, 0.82, 0.86, 1)  
                foreground_color: (0, 0, 0, 1)  
                font_size: sp(18)
                size_hint_y: None
                height: sp(40)

        BoxLayout:
            size_hint_y: None
            height: sp(40)
            spacing: 10

            Label:
                text: 'Senha:'
                size_hint_x: None
                width: sp(100)
                color: (0.98, 0.56, 0.65, 1)  
                font_size: sp(18)
            TextInput:
                id: senha
                password: True
                multiline: False
                background_color: (1, 0.82, 0.86, 1)  
                foreground_color: (0, 0, 0, 1)  
                font_size: sp(18)
                size_hint_y: None
                height: sp(40)
        
        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)

        Button:
            text: 'Login'
            background_normal: ''
            background_color: (0.98, 0.56, 0.65, 1)  
            color: (0, 0, 0, 1)  
            font_size: sp(18)
            size_hint_y: None
            height: sp(40)
            on_release: root.check_credentials()

        Button:
            text: 'Cadastrar'
            background_normal: ''
            background_color: (0.98, 0.56, 0.65, 1)  
            color: (0, 0, 0, 1)  
            font_size: sp(18)
            size_hint_y: None
            height: sp(40)
            on_release: root.register_user()

        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)
        
        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)

        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)
        
        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)

        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)
        
        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)

        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)
        
        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)

        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)
        
        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)

        Label:
            text: ' '
            size_hint_x: None
            width: sp(100)
            font_size: sp(18)
        
"""

Builder.load_string(kv_code)

class LoginScreen(BoxLayout):
    def check_credentials(self):
        email = self.ids.email.text
        senha = self.ids.senha.text
        requisicao = requests.get(f'{link}/Clientes/.json')
        data = requisicao.json()

        if data:
            for user in data.values():
                if user.get('Email') == email and str(user.get('Senha')) == senha:
                    print("Login bem-sucedido!")
                    return
        print("Email ou senha incorretos.")
        
    def register_user(self):
        email = self.ids.email.text
        senha = self.ids.senha.text
        dados = {'Email': email, 'Senha': senha}
        requisicao = requests.post(f'{link}/Clientes/.json', data=json.dumps(dados))
        print(requisicao)
        print(requisicao.text)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
