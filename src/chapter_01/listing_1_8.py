import time
import requests
import threading


def read_example() -> None:
    response = requests.get("https://www.google.ru")
    print(response.status_code)


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

thread_start = time.time()

thread_1.start()
thread_2.start()
print('Все потоки работают')

thread_1.join()
thread_2.join()

thread_end = time.time()

print(f"Многопоточное выполнение заняло {thread_end - thread_start:.4} с.")
