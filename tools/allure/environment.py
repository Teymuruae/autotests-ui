import platform
import sys

from config import settings


def create_allure_environment_file():
    env_list = [f'{key}={value}' for key, value in settings.model_dump().items()]
    env_list.append(f'os_info={platform.system()}, {platform.release()}')
    env_list.append(f'python_version={sys.version}')
    properties = '\n'.join(env_list)
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
