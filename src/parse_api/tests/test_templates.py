from src.parse_api import templates


def test_get_mocks():
    data = templates.get_mocks()
    assert len(data) > 0
