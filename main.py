def citire_lista():
    l = []
    givenstring = input("Dati lista cu numerele separate prin vrigula:")
    numbersasstring = givenstring.split(",")
    for x in numbersasstring:
        l.append(int(x))
    return l


def nr_neg(l):
    '''
    Afișeaza toate numerele negative nenule din listă
    :param l: lista de elemente
    :return: numerele negative nenule din listă
    '''
    rezultat = []
    for i in l:
        if i < 0:
            rezultat.append(i)
    return rezultat


def test_nr_neg():
    assert nr_neg([1, -2, 4, -3, 5, -6]) == [-2, -3, -6]
    assert nr_neg([1, 2, 3, 4, 5, 6, 7, 8, 9]) == []
    assert nr_neg([-1, -2, -3, -4]) == [-1, -2, -3, -4]


def ultimacifegala(n, l):
    '''
    Afișeaza cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param n: o cifra
    :param l: o lista de numere intregi
    :return: un numar intreg
    '''
    min = None
    for i in l:
        if i % 10 == n and (min == None or i < min):
            min = i
    return min


def test_ultimacifegala():
    assert ultimacifegala(6, [1, 2, 3, 4, 5]) == None
    assert ultimacifegala(9, [33, 39, 99, 69, 47]) == 39


def is_prime(n):
    """
    Determina daca un numar este prim
    :param n: o valoare intreaga
    :return: True, daca n este prim, respectiv False in caz contrar
    """
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False


def superprim(l):
    '''
    Afișeaza toate numerele din listă care sunt superprime. Un număr este superprim dacă este
    strict pozitiv și toate prefixele sale sunt prime.
    :param l: o lista de numere intregi
    :return:toate numerele din listă care sunt superprime
    '''
    global len
    rezultat = []
    for x in l:
        k = True
        cop = x
        xstr = str(x)
        while len(xstr) != 0 and k == True:
            if x <= 0 and is_prime(x) == False:
                k = False
            x = x // 10
            xstr = str(x)
        if k == True:
            rezultat.append(cop)
    return rezultat





def main():
    l = []
    test_nr_neg()
    test_ultimacifegala()
    test_is_prime()

    while True:
        print('1.Citire lista')
        print('2.Afiseaza toate numerele negative nenule din listă.')
        print('3.Afișeaza cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.')
        print(
            '4. Afișeaza toate numerele din listă care sunt superprime. Un număr este superprim dacă este strict pozitiv și toate prefixele sale sunt prime.')
        print('5. ')
        print('x.Iesire din program')
        opt = input('Alege optiunea: ')
        if opt == '1':
            l = citire_lista()
        elif opt == '2':
            l = input('Dati lista de numere:')
            print(nr_neg(l))
        elif opt == '3':
            l = input('Dati lista de numere:')
            n = int(input('Dati o cifra: '))
            print(ultimacifegala(n, l))
        elif opt == '4':
            l = input('Dati lista de numere:')
            print(superprim(l))
        elif opt == '5':
            l = input('Dati lista de numere:')
            print()
        elif opt == 'x':
            break
        else:
            print("optiune invalida")

main()

