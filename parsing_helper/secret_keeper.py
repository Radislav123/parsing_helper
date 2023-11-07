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

    def __init__(self, settings: "Settings") -> None:
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
