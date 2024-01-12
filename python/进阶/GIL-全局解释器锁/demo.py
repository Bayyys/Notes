from multiprocessing import Pool
from time import sleep
import time


def run(x):
    sleep(5)
    return x * x


if __name__ == "__main__":
    print(
        f"start time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}"
    )
    with Pool(5) as p:
        print(p.map(run, [1, 2, 3, 4, 5]))
    print(
        f"end time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}"
    )
