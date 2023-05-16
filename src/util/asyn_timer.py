import time
import functools
from typing import Callable, Any


def async_timed():
    def wrapper(function: Callable) -> Callable:
        @functools.wraps(function)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"Выполняется {function} с аргументами {args} {kwargs}")
            start = time.time()
            try:
                return await function(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"{function} завершилась за {total:.4f} с")
        return wrapped
    return wrapper