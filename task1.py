factor =0
def is_prime(prime_number):
    for i in range(1,prime_number+1):
        if prime_number % i ==0:
            global factor
            factor=factor+1
    if factor > 2:

        
        factor=0
        return False
            
        
    elif factor == 2:
        
        factor= 0
        return True          
            
        
            
          



        
    


for i in range(2,31):
    print(i,is_prime(i))