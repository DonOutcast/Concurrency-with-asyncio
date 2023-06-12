import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List


def partition(
        data: List,
        chunk_size: int,
) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    countre = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if countre.get(word):
            countre[word] = countre[word] + int(count)
        else:
            countre[word] = int(count)
    return countre


def merge_dictionaries(
        first: Dict[str, int],
        second: Dict[str, int]
) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


async def main(partition_size: int):
    with open("googlebooks-eng-all-1gram-20120701-a", encoding="UTF-8") as f:
        contents = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(
                    pool,
                    functools.partial(map_frequencies, chunk)
                )
                )
            intermediate_results = await asyncio.gather(*tasks)
            final_result = functools.reduce(merge_dictionaries, intermediate_results)

            print(f"Aardvark  встречается {final_result['Aardvark']} раз.")

            end = time.time()

            print(f"Время Mapreduce: {(end - start):.4f} секунд")


if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))

