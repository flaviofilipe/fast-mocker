from src.parse_api import templates


def test_get_templates():
    data = templates.get_templates()
    assert len(data) > 0
