def is_prime(x):
    # Complete the missing code here
    # The function takes in an integer and returns true
    # if it is prime. Otherwise, it returns false
    for i in range(2, x):
        if (x % i) == 0:
            return False
    else:
        return True
    
def is_twin_prime(x):	
    # Complete the missing code. The function takes in 
    # an integer and returns true if it is a twin prime.
    # Otherwise, it returns false. Hint: The function should
    # make use of the is_prime() function in some way
    twinAdd = x+2
    twinMinus = x-2
    if is_prime(x):
        if is_prime(twinAdd) and is_prime(twinMinus):
            return("true")
        else:
            return("false")

N = int(input())
for i in range(N):
    p = int(input())
    if is_twin_prime(p):
        print("true")
    else:
        print("false")

