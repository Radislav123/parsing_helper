import abc

from django.core.management import base

from parsing_helper import logger, settings


class BaseCommand(base.BaseCommand, abc.ABC):
    settings = settings.Settings()

    def __init__(self) -> None:
        super().__init__()
        self.logger = logger.Logger(self.__class__.__name__)
