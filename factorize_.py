from time import perf_counter
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count


def factorize(*numbers):
    result = []
    for num in numbers:
        sub_result = [1]
        for i in range(2, num):
            if num % i == 0:
                sub_result.append(i)
        sub_result.append(num)
        result.append(sub_result)
    return result


if __name__ == "__main__":
    start = perf_counter()
    nums = (128, 255, 99999, 10651060, 10651060, 10651060, 10651060, 10651060)
    factorize(*nums)
    print(f'Time without multiprocess: {perf_counter() - start:0.2f} sec.')

    start = perf_counter()
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        executor.map(factorize, nums)
    print(f'Time using multiprocess: {perf_counter() - start:0.2f} sec.')
