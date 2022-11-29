from typing import Any
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    flags: list
    comment: Any

#Передаем ысе данные и получаем экземпляр,
# датаклассы нужны для хранения определенных данных
a = User(
    name='Name',
    age=17,
    flags=[1, 2, 3],
    comment=True
)