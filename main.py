import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

kivy.require('2.0.0')

class WelcomeView(BoxLayout):
    def __init__(self):
        super(WelcomeView, self).__init__(orientation="vertical")

        # Create welcome label
        welcome_label = Label(text="Welcome to Immerge!", color=(0, 0, 0, 1), font_size=24)

        # Create logo image 
        logo = Image(source="logoimmerge.jpeg")


        # Create buttons for sign up and login
        sign_up_button = Button(text="Sign Up", on_release=self.sign_up)
        login_button = Button(text="Login", on_release=self.login)

        # Add the widgets to the layout
        self.add_widget(welcome_label)
        self.add_widget(logo)
        self.add_widget(sign_up_button)
        self.add_widget(login_button)

    def sign_up(self, instance):
        # Handle sign up logic
        # You can transition to the sign-up page or perform any other actions

        print("Sign Up button pressed")

    def login(self, instance):
        # Handle login logic
        # You can transition to the login page or perform any other actions

        print("Login button pressed")

class ImmergeApp(App):
    def build(self):
        return WelcomeView()

if __name__ == "__main__":
    ImmergeApp().run()

