#Create a list with size n
#check if n <= 2 or n > 99
    #return empty list
#make a boolean list of size n
#set index 0 and 1 to False
#loop through list starting from index 2 until sqrt of n
#(if the prime > sqrt(n) then it's multiples are outside the range of the list and all subsequent numbers set as True are prime numbers)
    #check if index i  in list is set to True
        #mark all multiples of i as False by iterating though the list incrementing by i
        #starting from i*i, up to n 
        #(we can start from i*i since i always starts as the smallest prime number 2,
        #so when we go though multiples of the next prime number smaller multiples will already be set as False)
        #set position as False
#
#return all the numbers set to True 



#import isqrt 
from math import isqrt

#define function, where input is a int, and out put is a list of int
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



if __name__ == '__main__':
    num = int(input("Ange gränsen för primtal du vill skriva ut?: "))
    print(sieve_of_eratosthenes(num))