
def prime_factorization(n):
    while n>1:
        k=smallest_prime_factor(n)
        n=n//k
        print(k)
        
def smallest_prime_factor(n):
        k=2
        while n%k != 0:
            k=k+1
        return k