def factorial(n:int)->int:
    res=1
    for numero in range(1,n+1): # for numero in range(n,0,-1):    
        res=res*numero #res*=numero        
    return res
    
def numero_combinatoria(m:int, n:int)->int:
    return factorial(m)/(factorial(n)*factorial(m-n))