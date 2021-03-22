def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def find_min(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


def find_max_and_min(arr):
    smallers = []
    biggers = []

    for i in range(1, len(arr), 2):
        if arr[i] > arr[i - 1]:
            biggers.append(arr[i])
            smallers.append(arr[i - 1])
        else:
            biggers.append(arr[i - 1])
            smallers.append(arr[i])

    if len(arr) % 2 == 1:
        if arr[-1] > arr[-2]:
            smallers.append(arr[-2])
            biggers.append(arr[-1])
        else:
            smallers.append(arr[-1])
            biggers.append(arr[-2])

    return find_max(biggers), find_min(smallers)


def number_generator(min, max, size):
    import random

    arr = []
    for i in range(size):
        arr.append((random.random()) * (max - min) + min)
    return arr


if __name__ == '__main__':
    numbers = number_generator(-100, 100, 5)
    print(numbers)
    print(find_max_and_min(numbers))
