from django.db import models

import logger
from parsing_helper.settings import Settings


class BaseModel(models.Model):
    class Meta:
        abstract = True

    settings = Settings()
    logger = logger.Logger(Meta.__qualname__[:-5])

    def __str__(self) -> str:
        if hasattr(self, "name"):
            string = self.name
        else:
            string = super().__str__()
        return string

    @classmethod
    def get_field_verbose_name(cls, field_name: str) -> str:
        return cls._meta.get_field(field_name).verbose_name
