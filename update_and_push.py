import subprocess

import update_version


def build() -> None:
    command = "venv/Scripts/python -m build"
    process = subprocess.Popen(command)
    process.wait()


def push() -> None:
    version = update_version.get_version()
    command = (f"venv/Scripts/twine upload dist/parsing_helper-{version}.tar.gz"
               f" dist/parsing_helper-{version}-py3-none-any.whl")
    process = subprocess.Popen(command)
    process.wait()


def main() -> None:
    update_version.main()
    build()
    push()


if __name__ == "__main__":
    main()
