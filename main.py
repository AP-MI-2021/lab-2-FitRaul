#Problema 1
def get_largest_prime_below(n):
    """
    Determina cel mai mare numar prim mai mic decat un numar dat.
    """
    maxim=0
    for x in range(2,n-1):
        ok=1
        for i in range(2,x//2):
            if x%i==0: ok=0
        if ok==1 and x>maxim: maxim=x
    return maxim


#Problema 5
def is_palindrome(n):
    """
    Verifica daca un numar dat este palindrom.
    """
    invers=0
    aux=n
    while aux!=0:
        cifra=aux%10
        invers=invers*10+cifra
        aux=aux//10
    if invers==n:
        return True
    else:
        return False
   
#Problema 12
def get_perfect_squares(start: int, end: int):
    """
    Determina toate patratele perfecte dintr un interval.
    :param start: primul capat al intervalului
    :param end: ultimul capat al intervalului
    :return:o lista cu toate patratele perfecte din intervalul inchis [start,end]
    """
    result=[]
    if start==1:result.append(start)
    ok=None
    for i in range(start,end+1):
        ok=0
        for j in range(1,i):
            if j*j==i: ok=1
        if ok==1: result.append(i)
    return result
 
    
def test_get_largest_prime_below():
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(9) == 7
    assert get_largest_prime_below(5) == 3
    

def test_is_palindrome():
    assert is_palindrome(131) == True
    assert is_palindrome(222) == True
    assert is_palindrome(214) == False

    
def test_get_perfect_squares():
    assert get_perfect_squares(1,16) == [1,4,9,16]
    assert get_perfect_squares(2,25) == [4,9,16,25]
    assert get_perfect_squares(5,36) == [9,16,25,36]

    
 def main():
    run=True
    while run:
        print("1.Determina cel mai mare numar prim mai mic decat un numar dat. ")
        print("2.Verifica daca un numar este palindrom")
        print("3. Determina toate patratele perfecte dintr un interval.")
        print("x. Iesire")
        optiune = input("Dati opțiunea: ")
        if optiune == "1":
           n=input('Introduceti un numar natural:')
           print('Cel mai mare numar prim mai mic decat n este {get_largest_prime_below(n)}')
        elif optiune == "2":
           n = int(input("Dati un nr :"))
           if is_palindrome(n):
               print("Nr este palindrom")
            else:
               print("Nr nu este palindrom")
        elif optiune == "3":
            start = input('Dati primul capat al intervalului')
            end = input('Dati ultimul capat al intervalului')
            print('Patratele perfecte din intervalul [{start},{end}] sunt {get_perfect_squares(start: int, end: int)}')
        elif optiune == "x":
            run = False
        else:
            print("Opțiune greșită! Reincercați!")

if __name__ == '__main__':
    main()
