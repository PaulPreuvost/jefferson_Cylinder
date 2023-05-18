import math
from os import system
import tkinter
import random

class main:
    def __init__(self):
        # Initialise les valeurs
        self.__alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.__length_Alphabet = len(self.__alphabet)
        self.__number_Of_Disk = 26
        self.__length_Of_Disk = self.__length_Alphabet
        self.Disk = []
        # Ajouter chaque ligne dans un ordre différent
        for i in range(self.__number_Of_Disk):
            #Ajoute l'alphabet dans un ordre différent à chaque ligne en ajoutant dans le self.Disk
            temp = self.__alphabet.copy()
            random.shuffle(temp)
            self.Disk.append(temp)
        self.row = 0
        self.column = 0

    def view_console(self):
        # Affichage console du cylindre
            #La prochaine ligne permet de "clear" le terminal:
                #Windows (NT): system("cls")
                #Mac OS/Linux (UNIX): system("clear")
        system("cls")
        print("Start")
        for self.row in range(self.__number_Of_Disk):
            for self.column in range(self.__length_Alphabet):
                print(self.Disk[self.row][self.column], end=' ')
            print()
        print("Affichage Console..... OK !")

    def read_TXT (self):
        # Lit le fichier input.txt et efface son contenu
        with open('txt/input.txt', 'w') as input:
            input.write('')
        print("Lecture Fichier..... OK !")

    def write_TXT (self):
        # Écrit la grille dans le fichier input.txt
        with open('txt/input.txt', 'w') as output:
            for self.row in range(self.__number_Of_Disk):
                for self.column in range(self.__length_Alphabet):
                    output.write(self.Disk[self.row][self.column])
                output.write('\n')
        print("Écriture Fichier..... OK !")

    def read_dictionnaire_TXT (self):
        # Lit le fichier input.txt et crée un dictionnaire
        dictionnaire = {}
        with open('txt/input.txt', 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                # Supprime les caractères en trop
                line = line.strip()
                # Ajoute la ligne dans le dictionnaire avec la clé correspondante (index 1 à 26)
                dictionnaire[i+1] = line
        print("Enregistrement Dictionnaire..... OK !")
        return dictionnaire







    def verif_permutation(self, key):
        #Vérifie si la clé est une permutation valide des entiers de 1 à 26.
        #key (list[int]): Une liste d'entiers représentant la clé.
        # #bool: True si la clé est valide, False sinon.
        if len(key) != len(set(key)):
            # Vérifie si les entiers de la clé sont uniques.
            return False
        if set(key) != set(range(1, len(key) + 1)):
            # Vérifie si les entiers de la clé sont tous compris entre 1 et 26.
            return False
        return True

    def generate_permutation(self, n):
    #Génère une permutation aléatoire de longueur n.
    # #n (int): La longueur de la permutation.
    # #lst_permutation[int]: Une liste d'entiers représentant la permutation.
        lst_permutation = list(range(26))
        random.shuffle(lst_permutation)
        return lst_permutation[:n]

    def encrypt_letter(self, letter, permutation):
        #Chiffre une lettre en utilisant une permutation.
        #letter (str): La lettre à chiffrer.
        #permutation (list[int]): Une liste d'entiers représentant la permutation à utiliser.
        # #cipher_letter: La lettre chiffrée.
        if letter == ' ':
            # Si la lettre est un espace, on la retourne telle quelle.
            return ' '
        index = self.__alphabet.index(letter)
            # On utilise la permutation pour chiffrer la lettre.
        cipher_letter = self.__alphabet[permutation[index]]
        return cipher_letter


    def encrypt_text(self, text, cylinders, key):
        #Chiffre un texte en utilisant des cylindres de permutation.
        #text (str): Le texte à chiffrer.
        #cylinders (list[list[int]]): Une liste de cylindres de permutation.
        #key (list[int]): Une liste d'entiers représentant la clé.
        #ciphertext: Le texte chiffré.
        if not self.verif_permutation(key):
            raise ValueError("La clé doit être une permutation des entiers compris entre 1 et 26.")
        n = len(cylinders)
        ciphertext = ''
        for i, letter in enumerate(text):
            permutation = cylinders[(i % n)]
            cipher_letter = self.encrypt_letter(letter, permutation)
            ciphertext += cipher_letter
        return ciphertext

    def decrypt_text(self, ciphertext, cylinders, key):
        #Déchiffre un texte chiffré en utilisant des cylindres de permutation.
        #ciphertext (str): Le texte chiffré.
        #cylinders (list[list[int]]): Une liste de cylindres de permutation.
        #key (list[int]): Une liste d'entiers représentant la clé.
        #plaintext: Le texte déchiffré.
        if not self.verif_permutation(key):
            # On vérifie que la clé est une permutation valide.
            raise ValueError("La clé doit être une permutation des entiers compris entre 1 et 26.")
        n = len(cylinders)
        plaintext = ''
        for i, cipher_letter in enumerate(ciphertext):
            permutation = cylinders[(i % n)]
            try:
                index = permutation.index(self.__alphabet.index(cipher_letter))
                plaintext += self.__alphabet[index]
            except ValueError:
                plaintext += cipher_letter
        return plaintext

    def decrypt_letter(self, cipher_letter, permutation):
        # Recherche de l'index de la lettre chiffrée dans l'alphabet
        cipher_index = self.__alphabet.index(cipher_letter)
        # Recherche de l'index correspondant dans la permutation fournie
        index = permutation.index(cipher_index)
        # Récupération de la lettre correspondant à l'index trouvé dans l'alphabet
        letter = self.__alphabet[index]
        # Retourne la lettre déchiffrée
        return letter

Launch = main()

key = [3, 1, 4, 2, 5]
cylinders = [Launch.generate_permutation(5) for _ in range(3)]


# Générer une permutation aléatoire
permutation = Launch.generate_permutation(26)

# Vérifier si la permutation est valide
print(Launch.verif_permutation([1, 2, 3, 4, 5]))  # False
print(Launch.verif_permutation(list(range(1, 27))))  # True

# Chiffrer et déchiffrer une lettre
print(Launch.encrypt_letter('A', permutation))  # Exemple de sortie : 'U'
print(Launch.decrypt_letter('U', permutation))  # Exemple de sortie : 'A'

# Afficher la grille de chiffrement dans la console
Launch.view_console()

# Écrire la grille de chiffrement dans un fichier texte
Launch.write_TXT()

cylinders = [permutation] * 3 # 3 cylindres identiques pour l'exemple
key = list(range(1, 27)) # clé valide pour l'exemple
ciphertext = Launch.encrypt_text('HELLO', cylinders, key)
plaintext = Launch.decrypt_text(ciphertext, cylinders, key)
print(ciphertext) # Exemple de sortie : 'UJNYAOWUJMY'
print(plaintext) # Exemple de sortie : 'HELLOWORLD'

dictionnaire = Launch.read_dictionnaire_TXT()
print(dictionnaire[1])