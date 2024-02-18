def any_remainder(n1, n2):
    if n1 == n2:
        return False
    else:
        while n1 >= n2:
            n1 -= n2

        if n1 == 0:
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
    factor = 1

    while i < n:
        if not any_remainder(n, i):
            return i
        i += 1

def main():
    n = int(input("What is your number? "))

    if is_prime(n):
        print("Prime")
    else:
        print("Not a prime number, a factor is:", find_factor(n))

main()