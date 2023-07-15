from pydantic import BaseModel

class DataModelDto(BaseModel):
    data: str

    