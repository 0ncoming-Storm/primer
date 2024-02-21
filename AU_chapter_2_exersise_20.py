def any_remainder(numerator, denumerator):
    if numerator == denumerator:
        return False
    else:
        while numerator >= denumerator:
            numerator -= denumerator

        if numerator == 0:
            return False
        else:
            return True


def is_prime(n):
    prime = True

    if n < 1:
        return False

    for i in range(2, n):
        if not any_remainder(n, i):
            prime = False
            return prime # not a prime number

    return prime # in case of n = 1 or 2 and any other prime numbers


def find_factor(n):
    i = 2
    factors = []

    while i < n:
        if not any_remainder(n, i):
            if is_prime(i):
                factors.append(i)
        i += 1
    return factors


def main():
    n = 1
    while int(n) > 0:
        try:
            n = input("What is your number? Or enter a negative number to quit: ")
            if is_prime(int(n)):
                print("Prime")
            elif int(n) > 0:
                print("Not a prime number, a factor are:", find_factor(int(n)))
            else:
                print("Not a prime number.")
        except ValueError:
            break
    print("Have a good day.")


main()
