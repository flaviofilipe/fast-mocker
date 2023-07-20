import json
from typing import Any, Mapping, Optional

from fastapi.responses import Response
from pydantic import BaseModel


class ParseResponse(BaseModel):
    media_type: str | None = None
    status_code: int = 200
    content: Any = None
    headers: Mapping[str, str] | None

    def get_response(self):
        """
        Returns the FastAPI Response base on the information given by YAML file
        >>> get_response()
        Response
        """
        content = (
            json.dumps(self.content)
            if type(self.content) == dict
            else self.content
        )
        return Response(
            status_code=self.status_code,
            content=content,
            media_type=self.media_type,
            headers=self.headers,
        )


class Template(BaseModel):
    entity: str
    name: str
    path: str
    method: str
    response: Optional[ParseResponse]


# class Parse(BaseModel):
#     entity: str
#     name: str
#     template: Template
