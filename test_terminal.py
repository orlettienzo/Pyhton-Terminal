def sum(liste):
    if len(liste) < 2:
        return "Len(list)Error"
    elif type(liste) != list:
        return "TypeError"
    elif any(type(element) != float for element in liste):
        return "ConvertToFloatError"

    somme = 0
    for i in liste:
        somme += i
    return somme
def test_sum():
    #Bool
    assert sum('not list') == "TypeError" #On a remplacé 'False' pour que ce soit plus
    #intuitif pour l'utilisateur
    assert sum([1, 2, 3]) == "ConvertToFloatError"
    assert sum([1.0]) == "Len(list)Error"


    # Égalités
    assert sum([1.0, 2.0]) == 3.0
    assert sum([1.0, 2.0, 3.0]) == 6.0
    assert sum([0.0, 0.0, 0.0]) == 0.0
    assert sum([-1.0, -2.0, -3.0]) == -6.0
    assert sum([1.0, 1.0, 1.0]) == 3.0
    assert sum([5.0, 5.0, 5.0]) == 15.0
    assert sum([10.0, 20.0, 30.0]) == 60.0
    assert sum([2.0, 3.0, 5.0]) == 10.0

    # Différences
    assert sum([1.0, 2.0, 3.0]) != 7.0
    assert sum([0.0, 1.0, 2.0]) != 5.0
    assert sum([-1.0, -1.0, -1.0]) != -2.0
    assert sum([1.0, 2.0, 3.0]) != 0.0
    assert sum([5.0, 5.0, 5.0]) != 10.0
    assert sum([10.0, 20.0, 30.0]) != 50.0
    assert sum([2.0, 2.0, 2.0]) != 5.0

    print('Tous les tests ont réussi')

test_sum()

def avg(liste):
    if len(liste) < 2:
        return "Len(list)Error"
    elif type(liste) != list:
        return "TypeError"
    elif any(type(element) != float for element in liste):
        return "ConvertToFloatError"

    somme = 0
    for i in liste:
        somme += i

    moyenne = somme/len(liste)
    return moyenne

def test_avg():
    # Bool
    assert avg('not list') == "TypeError"  # On a remplacé 'False' pour que ce soit plus intuitif pour l'utilisateur
    assert avg([1, 2, 3]) == "ConvertToFloatError"
    assert avg([1.0]) == "Len(list)Error"

    #Égalités
    assert avg([1.0, 2.0]) == 1.5
    assert avg([1.0, 2.0, 3.0]) == 2.0
    assert avg([0.0, 0.0, 0.0]) == 0.0
    assert avg([-1.0, -2.0, -3.0]) == -2.0
    assert avg([1.0, 1.0, 1.0]) == 1.0
    assert avg([5.0, 5.0, 5.0]) == 5.0
    assert avg([10.0, 20.0, 30.0]) == 20.0
    assert avg([2.0, 3.0, 5.0]) == 3.3333333333333335

    #Différences
    assert avg([1.0, 2.0, 3.0]) != 7.0
    assert avg([0.0, 1.0, 2.0]) != 5.0
    assert avg([-1.0, -1.0, -1.0]) != -2.0
    assert avg([1.0, 2.0, 3.0]) != 0.0
    assert avg([5.0, 5.0, 5.0]) != 10.0
    assert avg([10.0, 20.0, 30.0]) != 50.0
    assert avg([2.0, 2.0, 2.0]) != 5.0

    print('Tous les tests ont réussi')

test_avg()

def test_exit():
    assert exit() == False
    assert exit() != True
    print('Tous les tests ont réussi')

test_exit()


