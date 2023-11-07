import json

import git
import tap


def get_version() -> str:
    with open("project_data.json", 'r') as project_data_file:
        version = json.load(project_data_file)["version"]
    return version


class ArgumentParser(tap.Tap):
    message: str = ""  # сообщение, записываемое с тегом
    remove: bool = False  # если установлен, удаляет тег
    tag_name: str = get_version()  # задает специфичное, отличное от того, что указано в project_data.json, имя тега


def main() -> None:
    arguments = ArgumentParser().parse_args()
    repository = git.Repo()
    if arguments.remove:
        removing_tag = repository.tag(arguments.tag_name)
        repository.git.tag("-d", removing_tag)
        print(f"Удален тэг {arguments.tag_name}")
    else:
        repository.create_tag(get_version(), message = arguments.message)
        message = f"Добавлен тэг {arguments.tag_name}"
        if arguments.message:
            message += f" с сообщением \"{arguments.message}\""
        print(message)


if __name__ == "__main__":
    main()
