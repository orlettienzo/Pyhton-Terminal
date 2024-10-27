"""
1. Commencez avec une boucle while qui demande à l'utilisateur de donner des commandes.
2. Utilisez le code de la phase de préparation pour lire des commandes et réagir sur les commandes.
3. Écrivez au moins une fonction séparée pour chaque commande.
4. Utilisez des variables globales pour stocker l'état de l'outil (par exemple le nom du fichier).
5. Au début vous pouvez ignorer les erreurs: assurez-vous que l'outil fonctionne si l'utilisateur donne des commandes correctes.
6. Ensuite, améliorez le code afin que le programme continue quand une commande incorrecte est donnée.

"""

commands = ['file', 'info', 'words', 'search', 'sum', 'avg', 'help', 'exit']
additional_commands = ['clear']
fichier = 'None' #None == str pour éviter des erreurs (ex.: command 'info' avant spécification du fichier)
liste_of_words = [] #search avant words, donc on initialise une liste vide pour éviter des erreurs
running = True

def convert_to_float(element):
    try:
        element = float(element)
        return element
    except ValueError:
        print(f"Impossible to convert '{element}' to float")



#D'abord on crée les fonctions qui sont indépendants
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

def help():
    print("Voici les commandes à votre disponibilité:")
    for command in commands:
        print(f'\t> {command}')

#Fonctions pour le traitement des fichiers de texte
def load_file(name):
    fichier = name
    try:
        with open(name, 'r') as file:
            #print (f"Loaded {name}")
            return fichier

    except FileNotFoundError:
        print(f"File '{name}' not found.")

def print_load_file(name):
    try:
        with open(name, 'r') as file:
            print (f"Loaded {name}")
            #return fichier
    except:
        pass



def info(fichier):
    try:
        with open(fichier, 'r') as file:
            lines = len(file.readlines())

        with open(fichier, 'r') as file:
            sentences = file.readlines()

        chars = 0
        for line in sentences:
            line = line.strip()
            for letter in line:
                if letter != ' ' and letter != '\n':
                    chars += 1



        print(f"{lines} lines")
        print(f"{chars} caracters")

    except FileNotFoundError:
        print(f"File '{fichier}' not found.")

def words(fichier):
    try:
        with open(fichier, 'r') as file:
            text = file.read()

        list_of_words = text.split()
        #print(f"You now have access to the list of words from the text")
        return list_of_words

    except FileNotFoundError:
        print(f"File '{fichier}' not found.")

def print_words(fichier):
    try:
        with open(fichier, 'r') as file:
            text = file.read()

        #list_of_words = text.split()
        print(f"You now have access to the list of words from the text")
        #return list_of_words

    except FileNotFoundError:
        pass


def search(word, liste):
    if word in liste:
        print(f"'{word}' is in the list of words")

    else:
        liste_upper = [element.upper() for element in liste]
        word_to_compare = word.upper()
        if word_to_compare in liste_upper:
            print("Nice try! Try writing the word in a different way")
        else:
            print(f"'{word}' is not in the list of words")

def exit():
    return False #On va atribuer cete valeur à la variable running

def clear():
    print('\n' * 25)

#On va initialiser notre boucle
print(f"Welcome to your personalized tool!")
while running:
    command = input('> ')
    command = command.strip()
    if command == '':
        while command == '':
            print("Please enter a command")
            command = input('> ')
            command = command.strip()

    parameters = command.split()
    #print(parameters)


    if parameters[0] not in commands and parameters[0] not in additional_commands:
        print(f"Command '{parameters[0]}' not found")

    elif parameters[0] == 'file':
        if len(parameters) == 1:
            print("Please enter a file name")
        elif len(parameters) == 2:
            fichier = load_file(parameters[1])
            print_load_file(parameters[1])
            #print(fichier)
        else:
            print("Please enter only 1 file name")

    elif parameters[0] == 'info':
        info(fichier)

    elif parameters[0] == 'words':
        liste_of_words = words(fichier)
        print_words(fichier)

    elif parameters[0] == 'search':
        search(parameters[1], liste_of_words)

    elif parameters[0] == 'sum':
        if len(parameters) == 1 or len(parameters) == 2:
            print("Please enter at least two numbers")

        elif len(parameters) >= 3:
            numbers = [convert_to_float(element) for element in parameters[1:]]
            print(sum(numbers))
            #print(numbers)

    elif parameters[0] == 'avg':
        if len(parameters) == 1 or len(parameters) == 2:
            print("Please enter at least two numbers")

        elif len(parameters) >= 3:
            numbers = [convert_to_float(element) for element in parameters[1:]]
            print(avg(numbers))

    elif parameters[0] == 'help':
        help()


    elif parameters[0] == 'exit':
        running = exit()

    elif parameters[0] == 'clear':
        clear()

    else:
        print("Please enter a command")










    
















