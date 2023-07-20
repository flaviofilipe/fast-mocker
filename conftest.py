import pytest

from src.parse_api import model


@pytest.fixture
def parse_response_fixture() -> model.ParseResponse:
    return model.ParseResponse(
        media_type='application/json',
        status_code=200,
        content={'message': 'Hello Test'},
        headers={'fast-key': 'my-token'},
    )


@pytest.fixture
def template_fixture(parse_response_fixture) -> model.Template:
    return model.Template(
        path='/tests', method='get', response=parse_response_fixture
    )


@pytest.fixture
def parse_fixture(template_fixture) -> model.Parse:
    return model.Parse(
        entity='Tests', name='GetTest', template=template_fixture
    )
