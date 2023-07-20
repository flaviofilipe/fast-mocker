import os
from typing import Dict, List

import yaml
from yaml.loader import SafeLoader

from src.parse_api.model import Parse

FILE_DIR = os.path.dirname(os.path.realpath('__file__'))
MOCKS_PATH = '/mocks'
MOCKS_FULL_PATH = FILE_DIR + MOCKS_PATH

mock_files = next(os.walk(MOCKS_FULL_PATH))[2]


def load_mock_content(mock_file_path: str):
    path = f'{MOCKS_FULL_PATH}/{mock_file_path}'
    with open(path, 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))
        return data[0]


def format_mock_data(mock_content: dict) -> Dict[str, Parse]:
    entity = next(iter(mock_content))
    content = mock_content[entity]
    mock_parse = {
        entity: [
            Parse(entity=entity, name=name, template=template)
            for name, template in content.items()
        ]
    }

    return mock_parse


def get_mocks() -> List[Dict[str, Parse]]:
    response = list(map(load_mock_content, mock_files))
    return list(map(format_mock_data, response))
