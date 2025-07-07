from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

class InstaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.username_input = TextInput(hint_text='Enter Instagram username', multiline=False)
        fetch_button = Button(text='Fetch Profile')
        self.result_label = Label(text='')

        fetch_button.bind(on_press=self.fetch_profile)

        layout.add_widget(self.username_input)
        layout.add_widget(fetch_button)
        layout.add_widget(self.result_label)

        return layout

    def fetch_profile(self, instance):
        username = self.username_input.text.strip()
        sessionid = '61369225498%3A8dsp859NZDsN3G%3A28%3AAYdVLqEvdqSz8lBSEb8NtzESuugWBVyPrR8uHccz0w'

        headers = {
            "User-Agent": "Instagram 219.0.0.12.117 Android",
            "Cookie": f"sessionid={sessionid}"
        }

        url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"

        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            user = data['graphql']['user']
            result = f"Name: {user['full_name']}\nFollowers: {user['edge_followed_by']['count']}\nBio: {user['biography']}"
            self.result_label.text = result
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

InstaApp().run()