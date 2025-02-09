from pydantic import BaseModel
from typing import Optional, List
import traceback


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
    salary: Optional[float] = None # Optional variable with default value
    is_active: Optional[bool] = False # Optional variable with default value


class ClassRoom(BaseModel):
    room_number: int
    students: List[str]
    capacity: int


if __name__ == "__main__":
    person = Person(name="abc", age=12, city="xyz", marital_status=False)
    print(person)

    employee = Employee(id=1, name="abc", department="xyz")
    print(employee)

    class_room = ClassRoom(room_number=1, students=["1", "2"], capacity=10)
    print(class_room)

    try:
        invalid_val = ClassRoom(room_number=1, students=["1", 2], capacity=10)
    except ValueError as e:
        print(e)
        print(traceback.print_exc())

