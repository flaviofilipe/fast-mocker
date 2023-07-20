import os
from typing import List

import yaml
from yaml.loader import SafeLoader

from src.parse_api.model import Template

FILE_DIR = os.path.dirname(os.path.realpath('__file__'))
MOCKS_PATH = '/mocks'
MOCKS_FULL_PATH = FILE_DIR + MOCKS_PATH

MOCK_FILES = next(os.walk(MOCKS_FULL_PATH))[2]


def _load_mock_files(mock_file: str):
    """Loading file from the {{MOCKS_FULL_PATH}} path

    Args:
        mock_file (str): YAML file with the mock configuration

    Returns:
        _type_: _description_
    """
    path = f'{MOCKS_FULL_PATH}/{mock_file}'
    with open(path, 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))
        return data[0]


def _format_data(mock_content: dict) -> List[Template]:
    """Formatting data from yaml load and parsing to model.Parse entity

    Args:
        mock_content (dict): Dict content from YAML file

    Returns:
        Dict[str, Parse]: Returns a dict with a Entity and the data formatted
    """
    entity = next(iter(mock_content))
    content = mock_content[entity]
    mock_parse = [
        Template(entity=entity, name=name, **template)
        for name, template in content.items()
    ]

    return mock_parse


def get_templates() -> List[Template]:
    """
    Returns a list of data from all YAML mocks files

    >>> get_templates()
        List[Template]]

    Examples:
        >>> [
                {
                    'entity': 'Animals',
                    'name': 'GetAnimals',
                    'path': '/animals',
                    'method': 'get',
                    'response': {
                        'media_type': 'application/json',
                        'status_code': 200,
                        'content': 'Hello World', '
                        headers': None
                    }
                },
                ...
            ]

    """

    files_loaded = list(map(_load_mock_files, MOCK_FILES))
    response = [item for f in files_loaded for item in _format_data(f)]

    return response
