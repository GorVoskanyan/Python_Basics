def is_prime(number: int) -> bool:
    for div in range(2, int(number ** 0.5) + 1):
        if number % div == 0:
            return False

    return True


def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n


def main():
    n = int(input('>>> '))
    next_prime_n = next_prime(n)
    print(next_prime_n)


if __name__ == '__main__':
    main()