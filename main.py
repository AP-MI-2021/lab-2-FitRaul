def get_largest_prime_below(n):
    maxim=0
    for x in range(2,n-1):
        ok=1
        for i in range(2,x//2):
            if x%i==0: ok=0
        if ok==1 and x>maxim: maxim=x
    return maxim

def is_palindrome(n):
    invers=0
    aux=n
    while aux!=0:
        cifra=aux%10
        invers=invers*10+cifra
        aux=aux//10
    if invers==n:
        return 1
    else:
        return 0