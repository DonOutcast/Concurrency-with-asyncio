import asyncio
from enum import Enum


class ConnectionState(Enum):
    WAIT_INIT = 0
    INITIALIZING = 1
    INITIALIZED = 2


class Connection:

    def __init__(self):
        self._state = ConnectionState.WAIT_INIT
        self._condition = asyncio.Condition()

    async def initialize(self):
        await self._change_state(ConnectionState.INITIALIZING)
        print("initialize: Инициализация подключения....")
        await asyncio.sleep(3)
        print("initialize: Подключение инициализировано")
        await self._change_state(ConnectionState.INITIALIZED)

    async def execute(self, query: str):
        async with self._condition:
            print("execute: Ожидание инициализации подключения")
            await self._condition.wait_for(self._is_initialized)
            print(f"execute: Выполняется {query}")
            await asyncio.sleep(3)

    async def _change_state(self, state: ConnectionState):
        async with self._condition:
            print(f"change_state: Состояние изменятеся c {self._state} на {state}")
            self._state = state
            self._condition.notify_all()

    def _is_initialized(self):
        if self._state is not ConnectionState.INITIALIZED:
            print(f"_is_initialized: Инициализация подключения не закончена, состояние равно {self._state}")
            return False
        print(f"_is_initialized: Подключение инициализировано!")
        return True


async def main():
    connection = Connection()
    query_one = asyncio.create_task(connection.execute("SELECT * FROM table;"))
    query_two = asyncio.create_task(connection.execute("SELECT * FROM table;"))
    asyncio.create_task(connection.initialize())
    await query_one
    await query_two

if __name__ == "__main__":
    asyncio.run(main())
