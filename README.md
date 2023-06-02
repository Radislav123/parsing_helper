# Генерация истории изменений

## Генератор истории изменений
Ссылка на библиотеку - [*auto-changelog*](https://github.com/KeNaCo/auto-changelog). Сгенерировать историю:

```shell
auto-changelog
```

Сгенерировать историю, включая коммиты без релиза

```shell
auto-changelog -u
```

## Установка версии

За установку версии генератором истории изменений отвечают [*git-теги*](https://git-scm.com/docs/git-tag). Проект содержит файл
[*project_data.json*](project_data.json), содержащий текущую версию. Чтобы установить тег версии, достаточно использовать
[*update_version.py*](update_version.py):

```shell
python .\update_version.py
```

Удалить тег:

```shell
python .\update_version.py --remove
```

Посмотреть помощь по аргументам:

```shell
python .\update_version.py --help
```


Отправить тег в удаленный репозиторий ([*Stack Overflow*](https://stackoverflow.com/a/5195913/13186004)):

```shell
git push origin <tag_name>
git push origin 0.0.1
```


Отправить все теги в удаленный репозиторий:

```shell
git push --tags
```


# Генерация списка зависимостей
`pip freeze > .\requirements.txt`

## Использование списка зависимостей
`pip install -r .\requirements.txt`


# Публикация
[*Документация PyPI*](https://packaging.python.org/en/latest/flow/#upload-to-the-package-distribution-service)

```commandline
twine upload dist/parsing_helper-0.0.2.tar.gz dist/parsing_helper0.0.2-py3-none-any.whl
```
