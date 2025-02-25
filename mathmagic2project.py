def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_two_digit_primes():
    two_digit_primes = []
    for num in range(10, 100):
        if is_prime(num):
            two_digit_primes.append(num)
    return two_digit_primes

print(find_two_digit_primes())
