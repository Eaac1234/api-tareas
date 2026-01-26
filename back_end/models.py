from pydantic import BaseModel

class task(BaseModel):
    ID: int
    Title : str
    Descripcion :str
    State: int
    Created: str
    Last_Update: str



