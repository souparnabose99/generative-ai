from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str
    marital_status: bool

if __name__ == "__main__":
    person = Person(name="abc", age=12, city="xyz", marital_status=False)
    print(person)