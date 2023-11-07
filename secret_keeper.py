from parsing_helper import secret_keeper


class SecretKeeper(secret_keeper.SecretKeeper):
    Module = secret_keeper.SecretKeeper.Module

    class Maintainer(Module):
        username: str
        password: str

    maintainer: Maintainer

    def __init__(self, _) -> None:
        self.add_module("maintainer", "secrets/maintainer/credentials.json")
