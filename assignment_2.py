# Assingment 2: Get Maximum Prime Factor

def is_prime(x):
    """
     Method to check if the number is prime or not
    """
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True

def get_max_prime_factor(n):
    """
    function to get max prime factor of given number  
    """
    # Get list of prime numbers
    prime_numbers = [ i for i in range(n+1) if is_prime(i) == True ]  
    max_prime_factor = 0
     
    for i in prime_numbers:
        # Check if number is divisible by prime number in list 
        # and greater than previous prime factor
        if n % i == 0 and i > max_prime_factor:
             max_prime_factor = i
    return max_prime_factor


#driver code
if __name__ == "__main__":
    number = int(raw_input("Enter a number: "))
    max_prime_factor = get_max_prime_factor(number)
    print "Output : {}".format(max_prime_factor)
