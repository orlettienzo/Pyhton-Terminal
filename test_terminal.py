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

print('Test: sum()')
test_sum()
print()

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

print('Test: avg()')
test_avg()
print()


def convert_to_float(element):
    """Cette fonction convertie un string en float
    @pre:
        - element est un string
    @post
        - return float(element)
        - print error si ce n'est pas possible de faire
        la conversion
    """
    if type(element) != str:
        return False

    try:
        element = float(element)
        return element
    except ValueError:
        print(f"Impossible to convert '{element}' to float")

def test_convert_to_float():

    #Type(element) != str
    assert convert_to_float(12) == False
    assert convert_to_float(4.0) == False
    assert convert_to_float(1.9) == False
    assert convert_to_float(37) == False
    assert convert_to_float([1, 2, 3]) == False
    assert convert_to_float([1.0, 2.0, 3.0]) == False
    assert convert_to_float(['a', 'b', 'c']) == False

    #True conditions
    assert convert_to_float('4') == 4.0
    assert convert_to_float('4.2') == 4.2
    assert convert_to_float('-12') == -12.0
    assert convert_to_float('-483.75654') == -483.75654

    print('Tous les tests ont réussi')

print('Test: convert_to_float()')
test_convert_to_float()






