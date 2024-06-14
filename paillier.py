from sympy import lcm, mod_inverse, isprime
import secrets
import math
import random

bits = 10
global N
global phi_N
global g
global nu

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

def encrypt(c):

    r = random.randint(1, N - 1)
    
    while gcd(r, N) != 1:
        r = random.randint(1, N - 1)
    
    encrypted = (pow(g,c, N**2) * pow(r, N, N**2)) % N**2
        
    return encrypted


def encoder(m):

    list = []
    
    for c in m:
        list.append(encrypt(ord(c)))
    
    return list

def decrypt(num):
    c = num
    d = (c**phi_N)%(N**2)
    e = (d-1)/N
    
    decrypted = (e*nu)%N
    return decrypted
    

def decoder(encoded):
    s = ''
    
    for num in encoded:
        s += chr(int(decrypt(num)))
    
    return s

    
if __name__ == "__main__":
    while True:
        prime1 = generate_large_prime(bits)
        if(prime1 > 200):
            break
        
    while True:
        prime2 = generate_large_prime(bits)
        if(prime1 > 200 and prime2 != prime1):
            break
        
    N = prime1*prime2
    g = N+1
    phi_N = (prime1-1)*(prime2-1)
    nu = pow(phi_N,-1,N)
    
    print("public key : N =",N,",g =",N+1)
    
    # d = generate_privatekey(prime1,prime2,e)
    print("private key : N =",N,",phin =",phi_N,",nu =",nu)

    message = input("input message : ")
    
    encoded_message = encoder(message)
    
    
    
    print("encoded_message : ",encoded_message)
    
    print(decoder(encoded_message))