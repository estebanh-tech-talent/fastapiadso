from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    password: str

    class Config:
        orm_mode = True


class Item(BaseModel):
    # id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True


class Student(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    student_record: int

    class Config:
        orm_mode = True
