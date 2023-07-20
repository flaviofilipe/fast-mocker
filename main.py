import uvicorn
from fastapi import FastAPI

from src.parse_api.model import Template
from src.parse_api.templates import get_templates

app = FastAPI()


def map_routes(template: Template) -> None:
    """Map the content from YAML configuration with FastAPI route

    Args:
        parser (src.parse_api.model.Parse): YAML configuration parsed
    """
    app.add_api_route(
        path=template.path,
        endpoint=template.response.get_response,
        methods=[template.method],
    )


"""registering routes """
list(map(map_routes, get_templates()))


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
