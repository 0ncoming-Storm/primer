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
#    i = 2
#
#    while i < n:
#        if any_remainder(n, i):
#            return True # a prime number
#        else: 
#            return False # not a prime number
#
#        i += 1

    prime = True

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
            if is_prime(i) == True:
                factors.append(i)
        i += 1
    return factors

def main():
    n = int(input("What is your number? "))

    if is_prime(n):
        print("Prime")
    else:
        print("Not a prime number, a factor are:", find_factor(n))

main()