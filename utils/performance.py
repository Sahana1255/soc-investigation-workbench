import time
from contextlib import contextmanager


@contextmanager
def timer(name: str):

    start = time.perf_counter()

    yield

    elapsed = time.perf_counter() - start

    print(
        f"[PERFORMANCE] {name}: {elapsed:.2f} seconds"
    )