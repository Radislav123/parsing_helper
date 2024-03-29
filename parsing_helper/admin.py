import sys
from typing import Type

from django.contrib import admin

from parsing_helper import models
from .settings import Settings


def is_migration() -> bool:
    return "makemigrations" in sys.argv or "migrate" in sys.argv


def register_models(model_admins: list[Type["BaseAdmin"]]) -> None:
    for model_admin in model_admins:
        admin.site.register(model_admin.model, model_admin)


class BaseAdmin(admin.ModelAdmin):
    settings = Settings()
    hidden_fields = ()
    _fieldsets = ()
    # {вставляемое_поле: поле_перед_которым_вставляется}
    # {field: None} - вставится первым
    extra_list_display: dict[str, str] = {}
    not_required_fields: set[str] = set()

    def __init__(self, model, admin_site):
        self.list_display = [field for field in self._list_display if field not in self.hidden_fields]
        for field, before_field in self.extra_list_display.items():
            self.list_display.remove(field)
            if before_field is None:
                self.list_display.insert(0, field)
            else:
                self.list_display.insert(self.list_display.index(before_field), field)
        self.list_display = tuple(self.list_display)
        if self.fieldsets is not None:
            self.fieldsets += self._fieldsets
        else:
            self.fieldsets = self._fieldsets

        super().__init__(model, admin_site)

    @property
    def model(self) -> Type[models.BaseModel]:
        raise NotImplementedError()

    def get_form(self, request, obj = None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        for field_name in self.not_required_fields:
            form.base_fields[field_name].required = False
        return form

    @property
    def _list_display(self) -> tuple:
        # noinspection PyProtectedMember
        return tuple(field.name for field in self.model._meta.fields)


# пример использования register_models
model_admins_to_register = []
register_models(model_admins_to_register)
