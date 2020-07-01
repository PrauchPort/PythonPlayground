from typing import Dict, Any


class SingletonMeta(type):

    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":
    a = Singleton()
    b = Singleton()

    print(id(a) == id(b))
