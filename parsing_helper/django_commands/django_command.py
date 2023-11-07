import abc

from django.core.management.base import BaseCommand

from parsing_helper import logger, settings


class TelegramParserCommand(BaseCommand, abc.ABC):
    settings = settings.Settings()

    def __init__(self) -> None:
        super().__init__()
        self.logger = logger.Logger(self.__class__.__name__)
