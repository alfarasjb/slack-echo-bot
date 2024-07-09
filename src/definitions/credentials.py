import os

from dotenv import load_dotenv

from src.definitions.constants import SLACK_TOKEN, SIGNING_SECRET

load_dotenv()


class Credentials:
    @classmethod
    def slack_token(cls) -> str:
        return os.getenv(SLACK_TOKEN)

    @classmethod
    def slack_signing_secret(cls) -> str:
        return os.getenv(SIGNING_SECRET)


class EnvVariables:
    @classmethod
    def port(cls) -> int:
        return int(os.getenv('PORT', '5000'))
