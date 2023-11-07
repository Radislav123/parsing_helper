import logging

from secret_keeper import SecretKeeper


class Settings:
    APP_NAME = str

    def __init__(self):
        # Настройки Selenium
        # в секундах
        self.SELENIUM_DEFAULT_TIMEOUT = 5

        # Пути секретов
        self.SECRETS_FOLDER = "secrets"

        self.DATABASE_SECRETS_FOLDER = f"{self.SECRETS_FOLDER}/database"
        self.DATABASE_CREDENTIALS_PATH = f"{self.DATABASE_SECRETS_FOLDER}/credentials.json"

        self.DEVELOPER_SECRETS_FOLDER = f"{self.SECRETS_FOLDER}/developer"
        self.DEVELOPER_CREDENTIALS_PATH = f"{self.DEVELOPER_SECRETS_FOLDER}/credentials.json"

        self.DJANGO_SECRETS_FOLDER = f"{self.SECRETS_FOLDER}/django"
        self.DJANGO_CREDENTIALS_PATH = f"{self.DJANGO_SECRETS_FOLDER}/credentials.json"

        # Настройки логгера
        self.LOG_FORMAT = ("[%(asctime)s] - [%(levelname)s] - %(name)s -"
                           " (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
        self.LOG_FOLDER = "logs"
        self.CONSOLE_LOG_LEVEL = logging.DEBUG
        self.FILE_LOG_LEVEL = logging.DEBUG

        self.secrets = SecretKeeper(self)
