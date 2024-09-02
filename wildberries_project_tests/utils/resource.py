from pathlib import Path
import tests
from wildberries_project_tests import utils


def path(file_name):
    return str(Path(tests.__file__).parent.parent.joinpath(f'json_schemas/{file_name}'))


def path_from_project(relative_path: str):
    return (
        Path(utils.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
