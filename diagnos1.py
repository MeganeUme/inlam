#import isqrt 
from math import isqrt

#define function, where input is a int, and note that the function will retun a list[int]
def sieve_of_eratosthenes(n: int) -> list[int]:
    #if inputted value is 2 or less or over 99 return empty list
    if n <= 2 or n > 99:
        return []
    
    #make a boolean list with size n 
    is_prime = [True] * n
    #set 0 and 1 to False
    is_prime[0] = False
    is_prime[1] = False

    #loop though array starting from 2 and iterate though until isqrt(n)
    for i in range(2, isqrt(n)):
        #check if it is a Prime number
        if is_prime[i]:
            #Mark out all of the muliples of the primenumber as False
            #loop though starting from i*i, and end on n, incrementing by i steps 
            for x in range(i*i, n, i):
                is_prime[x] = False

    #return list of all numbers marked as True
    return [i for i in range(n) if is_prime[i]]

def main():
    num = int(input("Ange gränsen för primtal du vill skriva ut?: "))
    print(sieve_of_eratosthenes(num))

if __name__ == '__main__':
    main()