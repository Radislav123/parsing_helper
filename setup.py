import json

from setuptools import setup


PROJECT_DATA_PATH = "project_data.json"
PROJECT_REQUIREMENTS_PATH = "requirements.txt"

with open(PROJECT_DATA_PATH, 'r') as project_data_file:
    project_data = json.load(project_data_file)

with open(PROJECT_REQUIREMENTS_PATH, 'r') as project_requirements_file:
    requirements_list = ["selenium", "django"]
    requirements = []
    for requirement in requirements_list:
        for project_requirement in project_requirements_file:
            project_requirement_clean = project_requirement.strip().replace("\x00", "")
            if requirement in project_requirement_clean:
                requirements.append(project_requirement_clean)

setup(
    author = "Radislav Vlasov",
    author_email = "radislavvlasov@gmail.com",
    name = project_data["package_name"],
    version = project_data["version"],
    install_requires = requirements,
    data_files = [("", [PROJECT_DATA_PATH, PROJECT_REQUIREMENTS_PATH])]
)
