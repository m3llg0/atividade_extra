from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="users_db"
)

cursor = db.cursor()

cores = {
    'primaria': '#FFC0CB',  
    'secundaria': '#000000',  
    'terciaria': '#FFD1DC'  
}

kv_code = f"""
BoxLayout:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    BoxLayout:
        size_hint_y: None
        height: sp(40)

        Label:
            text: 'Usuário:'
            size_hint_x: None
            width: sp(100)
            color: {cores['secundaria']}
        TextInput:
            id: usuario
            multiline: False
            background_color: {cores['terciaria']}
            foreground_color: {cores['secundaria']}

    BoxLayout:
        size_hint_y: None
        height: sp(40)

        Label:
            text: 'Senha:'
            size_hint_x: None
            width: sp(100)
            color: {cores['secundaria']}
        TextInput:
            id: senha
            password: True
            multiline: False
            background_color: {cores['terciaria']}
            foreground_color: {cores['secundaria']}

    Button:
        text: 'Login'
        background_normal: ''
        background_color: {cores['primaria']}
        on_release: app.check_credentials()

    Button:
        text: 'Cadastrar'
        background_normal: ''
        background_color: {cores['primaria']}
        on_release: app.register_user()
"""

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Builder.load_string(kv_code))

    def check_credentials(self):
        username = self.ids.usuario.text
        password = self.password.text

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos.")

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
