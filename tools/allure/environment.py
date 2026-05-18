from config import settings


def create_allure_environment_file():
    env_list = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(env_list)
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
