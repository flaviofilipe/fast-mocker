import uvicorn
from fastapi import FastAPI

from src.parse_api.model import Parse
from src.parse_api.templates import get_mocks

app = FastAPI()


def map_routes(parser: Parse):
    app.add_api_route(
        path=parser.template.path,
        endpoint=parser.template.response.get_response,
        methods=[parser.template.method],
    )


list(map(lambda m: list(map(map_routes, m[next(iter(m))])), get_mocks()))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
