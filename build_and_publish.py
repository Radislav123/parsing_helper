import subprocess

import secret_keeper
import update_version
from parsing_helper import settings


secrets = secret_keeper.SecretKeeper(settings.Settings())


def build() -> None:
    command = "venv/Scripts/python -m build"
    process = subprocess.Popen(command)
    process.wait()


def push() -> None:
    version = update_version.get_version()
    username = secrets.maintainer.username
    password = secrets.maintainer.password
    command = (f"venv/Scripts/twine upload dist/parsing_helper-{version}.tar.gz"
               f" dist/parsing_helper-{version}-py3-none-any.whl"
               f" -u {username} -p {password}")
    process = subprocess.Popen(command)
    process.wait()


def main() -> None:
    build()
    push()


if __name__ == "__main__":
    main()
