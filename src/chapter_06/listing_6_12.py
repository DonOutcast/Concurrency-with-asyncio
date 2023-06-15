from multiprocessing import Process, Value


def increment_value(shard_int: Value):
    shard_int.get_lock().acquire()
    shard_int.value = shard_int.value + 1
    shard_int.get_lock().release()


if __name__ == "__main__":
    for _ in range(100):
        integer = Value('i', 0)
        procs = [
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,))
        ]
        [p.start() for p in procs]
        [p.join() for p in procs]
        print(integer.value)
        assert (integer.value == 2)

