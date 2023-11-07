import json
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from parsing_helper.settings import Settings


class SecretKeeper:
    class Module:
        name: str
        secrets_path: str
        json: dict
        secret_keeper: "SecretKeeper"

    class SQLite(Module):
        ENGINE: str
        NAME: str

    class DjangoAdminUser(Module):
        username: str
        email: str
        password: str

    class Django(Module):
        secret_key: str

    class Developer(Module):
        pc_name: str

    database: SQLite
    django_admin_user: DjangoAdminUser
    developer: Developer
    django: Django

    def __init__(self, settings: "Settings") -> None:
        self.add_module("database", settings.DATABASE_CREDENTIALS_PATH)
        self.add_module("admin_user", settings.ADMIN_USER_CREDENTIALS_PATH)
        self.add_module("django", settings.DJANGO_CREDENTIALS_PATH)
        try:
            self.add_module("developer", settings.DEVELOPER_CREDENTIALS_PATH)
        except FileNotFoundError:
            pass

    @staticmethod
    def read_json(path: str) -> dict:
        with open(path, 'r') as file:
            data = json.load(file)
        return data

    def add_module(self, name: str, secrets_path: str) -> None:
        json_dict = self.read_json(secrets_path)
        module = type(name, (self.Module,), json_dict)()
        module.name = name
        module.secrets_path = secrets_path
        module.json = json_dict
        module.secret_keeper = self
        setattr(self, name, module)
