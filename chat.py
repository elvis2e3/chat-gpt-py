import flet as ft
from gpt import chat_gpt

class Message():
    def __init__(self, user: str, text: str):
        self.user = user
        self.text = text

def main(page: ft.Page):

    chat = ft.Column()
    new_message = ft.TextField()

    def on_message(message: Message):
        chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        message = new_message.value
        page.pubsub.send_all(Message(user='elvis2e3', text=message))
        page.pubsub.send_all(Message(user='GPT', text=chat_gpt(message)))
        new_message.value = ""
        page.update()

    page.add(
        chat, 
        ft.Row([
            new_message, 
            ft.ElevatedButton("Send", on_click=send_click)
        ]))

ft.app(target=main)
