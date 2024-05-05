def is_prime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return("False")
    return("True")
def add(a,b):
    return (a+b)
