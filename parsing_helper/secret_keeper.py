import json


class SecretKeeper:
    class Module:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def read_json(path: str) -> dict:
        with open(path, 'r') as file:
            data = json.load(file)
        return data

    def add_module(self, name: str, settings_path: str):
        module = type(name, (self.Module,), self.read_json(settings_path))
        setattr(self, name, module)