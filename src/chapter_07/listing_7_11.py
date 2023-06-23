import time
from threading import Lock, Thread

lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a:
        print("Захвачена блокировака а из метода а!")
        time.sleep(1)
        with lock_b:
            print("Захвачены обе блокировки из метода а!")


def b():
    with lock_b:
        print("Захвачена блокировка b из метода b!")
        with lock_a:
            print("Захвачены обе блокировки")


thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
