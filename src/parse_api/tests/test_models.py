import json

from src.parse_api import model


def test_parse_response(parse_response_fixture: model.ParseResponse):
    response = parse_response_fixture.get_response()
    headers = response.raw_headers
    body = json.loads(response.body.decode())

    assert any(b'fast-key' == chave for chave, _ in headers)
    assert response.status_code == 200
    assert response.media_type == 'application/json'
    assert body['message'] == 'Hello Test'


def test_template(template_fixture: model.Template):
    assert template_fixture.entity == 'Tests'
    assert template_fixture.name == 'GetTest'
    assert template_fixture.path == '/tests'
    assert template_fixture.method == 'get'
