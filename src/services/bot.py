from slack_bolt import App
from slack_sdk import WebClient

from src.definitions.credentials import Credentials, EnvVariables


class SlackBot:
    def __init__(self):
        self.app = self._init_app()
        self.client = WebClient(token=Credentials.slack_token())
        self.setup_events()

    @staticmethod
    def _init_app():
        app = App(
            token=Credentials.slack_token(),
            signing_secret=Credentials.slack_signing_secret()
        )
        return app

    def setup_events(self):
        @self.app.event('message')
        def handle_app_message_events(client, body, logger):
            text = body['event']['text']
            channel = body['event']['channel']
            self.client.chat_postMessage(channel=channel, text=text)

    def start(self):
        self.app.start(port=EnvVariables.port())
