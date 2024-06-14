import sympy
import secrets
import math

bits = 10

def generate_large_prime(bits):
    while True:
        candidate = secrets.randbits(bits)
        candidate |= 1
        if sympy.isprime(candidate):
            return candidate

def generate_publickey(prime1,prime2):
    phi_n = (prime1-1)*(prime2-1)
    e = 2
    while(True):
        if(math.gcd(e,phi_n) == 1):
            return e
        e += 1
        
def generate_privatekey(prime1,prime2,e):
    phi_n = (prime1-1)*(prime2-1)
    return pow(e,-1,phi_n)                          #inverse of modular

def encrypt(c,n,e):
    
    encrypted = 1
    while e > 0:

        encrypted *= c
        encrypted %= n
        e -= 1
        
    return encrypted


def encoder(m,n,e):

    list = []
    
    for c in m:
        list.append(encrypt(ord(c),n,e))
    
    return list

def decrypt(num,n,d):
    
    decrypted = 1
    
    
    while d > 0:
        decrypted *= num
        decrypted %= n
        d -= 1
    
    return decrypted
    

def decoder(encoded,n,d):
    s = ''
    
    for num in encoded:
        s += chr(decrypt(num,n,d))
    
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
    
    e = generate_publickey(prime1,prime2)
    print("public key : N =",N,",e =",e)
    
    d = generate_privatekey(prime1,prime2,e)
    print("private key : N =",N,",d =",d)

    message = input("input message : ")
    
    encoded_message = encoder(message,N,e)
    
    print("encode_text : ",encoded_message)
    
    print(decoder(encoded_message,N,d))