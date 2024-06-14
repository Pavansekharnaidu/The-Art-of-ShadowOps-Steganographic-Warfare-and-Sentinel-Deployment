from sympy import lcm, mod_inverse, isprime
import secrets
import math
import random

bits = 10
global alpha
global beta
global a
global p

def gcd(a,b):
    if b == 0 :
        return a
    return gcd(b,a%b)

def generate_large_prime(bits):
    while True:
        candidate = secrets.randbits(bits)
        candidate |= 1
        if isprime(candidate):
            return candidate

def prime_factors(n):
    factors = set()
    
    while n % 2 == 0:
        factors.add(2)
        n //= 2
        
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            factors.add(i)
            n //= i
            
    if n > 2:
        factors.add(n)
    
    return factors
    
    
def isprimitive_root(alpha,p):
    """Check if alpha is a primitive root modulo p. eulerian algo """
    if gcd(alpha, p) != 1:
        return False
    order = p - 1
    factors = prime_factors(order)
    for factor in factors:
        if pow(alpha, order // factor, p) == 1:
            return False
    return True 
    

def primitive_root(p):
    
    for i in range(2,p):
        if isprimitive_root(i,p):
            return i
        
    return None
    
    
def encrypt(c):

    k = random.randint(1, p-2)
    
    c1 = pow(alpha,k,p)
    c2 = (c*(beta**k))%p
    encrypted = (c1,c2)
        
    return encrypted


def encoder(m):

    list = []
    
    for c in m:
        list.append(encrypt(ord(c)))
    
    return list   


def decrypt(pair):

    gama = pair[0]
    delta = pair[1]
    
    c1 = gama**(p-1-a)
    c2 = delta
    
    return (c1*c2) % p

def decoder(encoded):
    s = ''
    
    for pair in encoded:
        s += chr(int(decrypt(pair)))
    
    return s

if __name__ == "__main__":
    while True:
        prime1 = generate_large_prime(bits)
        if(prime1 > 200):
            break
    p = prime1
    print(p)
    a = random.randint(0,p-1)
    private_key = a
    print("private key:",a)
    alpha = primitive_root(p)
    beta = pow(alpha,a,p)
    
    public_key = {p,alpha,beta}
    print("public key : {alpha,a,p} =",public_key)
    
    message = input("input message :")
    encoded = encoder(message)
    
    decoded = decoder(encoded)
    print("encoded_message :" , encoded)
    print(decoded)