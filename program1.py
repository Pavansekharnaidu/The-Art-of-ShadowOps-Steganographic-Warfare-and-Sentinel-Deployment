def gcd_on(a,b):
    m = min(a,b)
    
    while m>0:
        if(a % m == 0 and b % m == 0):
            break
        else :
            m = m-1
    
    return m
    

def gcd_eulerian(a,b):
    if b == 0 :
        return a
    
    return gcd_eulerian(b,a%b)









if __name__ == "__main__":
    print("This is the program which outputs the gcd from the given two numbers :")

    a = int(input("enter the first number :"))
    b = int(input("enter the second number :"))
    
    print("calculating gcd of",a ,"and",b,"using two diffent methods")
    print("")
    print("gcd using O(n) program",gcd_on(a,b))
    print("gcd calculated using eulerian approach",gcd_eulerian(a,b))
    