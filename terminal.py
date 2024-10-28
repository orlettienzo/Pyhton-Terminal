#Mission 6
#Andrade Orletti, Enzo
#Profirov, Viktor

#Liste pour stocker les commandes que l'utilisateur aura acces
commands = ['file', 'info', 'words', 'search', 'sum', 'avg', 'help', 'exit']
#Commandes supplémentaires
additional_commands = ['clear', 'today']

#None est un str car si l'utilisateur ne spécifie pas un nom d'un fichier, le code ne s'arretera pas
fichier = 'None'
liste_of_words = [] #on initialise une liste vide pour éviter des erreurs
# (ex: utilisateur essaie chercher un mot avant de spécifier le fichier et de le transformer
# en une liste de mots : > words)

running = True #Tant que l'utilisateur n'utilise pas le commande 'exit':
# --> running sera = True
# -->  le programme continue à marcher

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



def sum(liste):
    """Cette fonction calcule la somme des elements de la liste
    @pre:
        - type(liste) == lst
        - type(elements de la liste) == float
    @post:
        - retourne la somme des elements de la liste
        - print le message d'erreur spécifique si ce n'est pas possible
    """

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
    """Cette fonction calcule la somme des elements de la liste
        @pre:
            - type(liste) == lst
            - type(elements de la liste) == float
        @post:
            - retourne la somme des elements de la liste
            - retourne le message d'erreur spécifique si ce n'est pas possible
        """

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
    """Cette fonction affiche les comandes disponibles
    pour l'utilisateur
    @pre:
        /
    @post:
        - print des commandes

    """

    print("Voici les commandes à votre disponibilité:")
    for command in commands:
        print(f'\t> {command}')
    for new_command in additional_commands:
        print(f'\t> {new_command}')

#Fonctions pour le traitement des fichiers de texte
def load_file(name):
    """Cette fonction ouvre le fichier et retourne son nom
    @pre:
        - type(name) == str
        - name est le nom d'un fichier qui existe dans le même dossier du code
    @post:
        - retourne le nom du fichier
        - affiche un message d'erreur si ce n'est pas possible"""

    fichier = name
    try:
        with open(name, 'r') as file:
            #print (f"Loaded {name}")
            return fichier

    except FileNotFoundError:
        print(f"File '{name}' not found.")

def print_load_file(name):
    """Cette fonction affiche l'état de telechargement du fichier"""
    try:
        with open(name, 'r') as file:
            print (f"Loaded {name}")
            #return fichier
    except:
        pass



def info(fichier):
    """Cette fonction affiche la quantité de lignes et de
    caracteres du fichier"""

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
    """Cette fonction transforme le texte du fichier
     en une liste de mots"""

    try:
        with open(fichier, 'r') as file:
            text = file.read()

        list_of_words = text.split()
        #print(f"You now have access to the list of words from the text")
        return list_of_words

    except FileNotFoundError:
        print(f"File '{fichier}' not found.")

def print_words(fichier):
    """Cette fonction informe l'utilisateur s'il a accès
    ou non à la liste de mots du fichier"""

    try:
        with open(fichier, 'r') as file:
            text = file.read()

        #list_of_words = text.split()
        print(f"You now have access to the list of words from the text")
        #return list_of_words

    except FileNotFoundError:
        pass
def search(word, liste):
    """Cette fonction cherche le mot souhaité
    par l'utilisateur parmi les mots du texte
    du fichier"""

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
    """Cette fonction permet l'utlisateur
    à arreter le programme"""
    return False #On va atribuer cete valeur à la variable running

#--------------------
#Additional commands
#--------------------
def clear():
    print('\n' * 25)


from datetime import datetime

def today_date():
    #Formatation de la date en string
    return datetime.today().strftime('%d/%m/%Y')

def spent_time(value):
    #Affiche combien de temps le programme a
    # été en cours d'execution
    return f"User report: you spent {value}"

#--------------------
#Boucle while
#--------------------

print(f"Welcome to your personalized tool!")
start_time = datetime.now() #varible utilisée dans le calcul de temps d'execution
while running: # <=> while True
    command = input('> ')
    command = command.strip()
    if command == '': #Traitement d'erreur: L'utilisateur n'écrit rien
        while command == '':
            print("Please enter a command")
            command = input('> ')
            command = command.strip()

    parameters = command.split()
    #print(parameters)


    if parameters[0] not in commands and parameters[0] not in additional_commands:
        print(f"Command '{parameters[0]}' not found") #commande ne se trouve pas parmi les commandes possibles

    elif parameters[0] == 'file':
        if len(parameters) == 1: #Utilisateur a écrit seulement 'file'
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
        if len(parameters) == 1 or len(parameters) == 2: #On demande au moins 2 nombres à l'utilisateur
            print("Please enter at least two numbers")

        elif len(parameters) >= 3:
            numbers = [convert_to_float(element) for element in parameters[1:]]
            print(sum(numbers))
            #print(numbers)

    elif parameters[0] == 'avg':
        if len(parameters) == 1 or len(parameters) == 2: #On demande au moins 2 nombres à l'utilisateur
            print("Please enter at least two numbers")

        elif len(parameters) >= 3:
            numbers = [convert_to_float(element) for element in parameters[1:]]
            print(avg(numbers))

    elif parameters[0] == 'help':
        help()


    elif parameters[0] == 'exit':
        end_time = datetime.now()
        total_time = end_time - start_time #Calcul temps d'execution du programme
        print(spent_time(total_time))
        running = exit()

    #Commandes supplémentaires
    elif parameters[0] == 'clear':
        clear()

    elif parameters[0] == 'today':
        print(today_date())

    else:
        print("Please enter a command")










    
















