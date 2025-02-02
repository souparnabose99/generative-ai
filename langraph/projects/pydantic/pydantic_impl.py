from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str
    marital_status: bool

