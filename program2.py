def gcd_2(a,b):
    if(b == 0) :
        return a
    return gcd_2(b,a%b)

def gcd(a,b,c):
    return gcd_2(a,gcd_2(b,c))

def find_k(a,b,c,d):
    g = gcd_2(a,b)
    n = 0 
    
    while True:
        if((d - n*g) % c == 0) :
            return (d - n*g)/c
        n += 1
        
def extended_gcd(a, b):
    if isinstance(a, int):
        print(f"{a} is an integer.")
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)

def mul_inverse(a, b):
    if isinstance(a, int):
        print(f"{a} is an integer.")
    gcd, x, y = extended_gcd(a, b)
    return x % b

if __name__ == "__main__":
   print("This  program finds the solution of linear equation Ax+By+Cz = D")
   A = int(input("enter A "))
   B = int(input("enter B "))
   C = int(input("enter C "))
   D = int(input("enter D "))
   
   g = gcd(A,B,C)
   if D % g != 0:
       print("No solution for given input")
       
   else:
       a = A/g
       b = B/g
       c = C/g
       d = D/g
       
       z = find_k(a,b,c,d)
       
       a = a/gcd_2(a,b)
       b = b/gcd_2(a,b)
       rhs = (d - c*z)/gcd_2(a,b)
       
       inv = mul_inverse(a,b)
       x = (inv*(rhs))%b
       
       y = (D - (A*x)-(C*z))/B
       
       print("x =",x,"y =",y,"z =",z)