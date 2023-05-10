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

    def view_Console(self):
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

    def read_Dictionnaire_TXT (self):
        # Lit le fichier input.txt et crée un dictionnaire
        dictionnaire = {}
        with open('TXT/input.txt', 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                # Supprime les caractères en trop
                line = line.strip()
                # Ajoute la ligne dans le dictionnaire avec la clé correspondante (index 1 à 26)
                dictionnaire[i+1] = line
        print("Enregistrement Dictionnaire..... OK !")
        return dictionnaire

    def verif_Permutation(self, n, lst):
        # Vérification si une liste de n entiers est une permutation des entiers compris (au sens large) entre 1 et n
        print("Vérification Permutation..... Start !")
        if set(lst) == set(range(1, n+1)):
            print("Vérification Permutation..... OK !")
            return True
        print("Vérification Permutation..... FAILED !")
        return False

    def generate_Permutation(self, n):
        # Génération d'une permutation des 26 lettres de l'alphabet en majuscules
        print("Génération Permutation..... Start !")
        permutation = self.__alphabet.copy()
        random.shuffle(permutation)
        print("Génération Permutation..... OK !")
        return permutation

    def chiffrement(self, lettre, permutation):
        # Chiffrement d'une lettre relativement à une permutation des 26 lettres de l’alphabet en majuscules :
        # on retourne la lettre située 6 positions après elle dans la permutation.
        # On suppose bien sûr que l’alphabet en question est circulaire.
        print("Chiffrement..... Start !")
        idx_perm = permutation.index(lettre)
        lettre_chiffree = permutation[(idx_perm+6)%len(permutation)]
        print(f"Lettre à chiffrer : {lettre} | Lettre chiffrée : {lettre_chiffree}")
        print("Chiffrement..... OK !")
        return lettre_chiffree

    def dechiffrement(self, lettre_chiffree, permutation):
        # Déchiffrement d'une lettre chiffrée relativement à une permutation des 26 lettres de l’alphabet en majuscules :
        # on retourne la lettre située 6 positions avant elle dans la permutation.
        # On suppose bien sûr que l’alphabet en question est circulaire.
        print("Déchiffrement..... Start !")
        idx_perm = permutation.index(lettre_chiffree)
        lettre = permutation[(idx_perm-6)%len(permutation)]
        print(f"Lettre à déchiffrer : {lettre_chiffree} | Lettre déchiffrée : {lettre}")
        print("Déchiffrement..... OK !")
        return lettre


Launch = main()
Launch.verif_Permutation(5, [1, 2, 3, 4, 5])
Launch.verif_Permutation(26, list(range(1, 27)))
permutation = Launch.generate_Permutation(26)
Launch.chiffrement('A', permutation)
Launch.dechiffrement('A', permutation)


Launch.view_Console()
Launch.read_TXT()
Launch.write_TXT()
dictionnaire = Launch.read_Dictionnaire_TXT()
print(dictionnaire[1])