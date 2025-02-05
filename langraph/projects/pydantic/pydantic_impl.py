from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    name: str
    age: int
    city: str
    marital_status: bool

# Optional variables
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: Optional[float] = None #
    is_active: Optional[bool]


if __name__ == "__main__":
    person = Person(name="abc", age=12, city="xyz", marital_status=False)
    print(person)