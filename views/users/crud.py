"""
CREAT
READ
UPDATE
DELITE
"""

from .schemas import User, UserIn
from pydantic import BaseModel


class UsersStorage(BaseModel):
    counter: int = 0
    cache_by_id: dict[int, User] = {}
    cache_by_token: dict[str, User] = {}

    @property
    def next_id(self) -> int:
        self.counter += 1
        return self.counter


storage = UsersStorage()


def get_users() -> list[User]:
    return list(storage.cache_by_id.values())


def create_user(user_in: UserIn) -> User:
    # Генерируем новый id
    new_id = storage.next_id
    # Создаём объект User
    user = User(id=new_id, **user_in.dict())
    # Сохраняем в хранилище
    storage.cache_by_id[user.id] = user
    storage.cache_by_token[user.token] = user
    # Возвращаем экземпляр, а не класс
    print("new user", user)
    return user


def get_user(user_id: int) -> User | None:
    return storage.cache_by_id.get(user_id)


def get_user_by_token(token: str) -> User | None:
    return storage.cache_by_token.get(token)


def delete_user(user_id: int) -> None:
    return storage.cache_by_id.pop(user_id, None)
