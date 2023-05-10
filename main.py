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
            #Ajoute l'alphabet dans le bon ordre à la ligne 6, l'ajoutant dans le self.Disk
            if i == 5:  # sixième ligne
                self.Disk.append(self.__alphabet.copy())  # copie de l'alphabet
            #Ajoute l'alphabet dans un ordre différent à chaque ligne en ajoutant dans le self.Disk
            else:
                temp = self.__alphabet.copy()
                random.shuffle(temp)
                self.Disk.append(temp)
        self.row = 0
        self.column = 0

    def view_Console(self):
        # Affichage console du cylindre
            #La prochaine ligne permet de "clear" le terminal:
                #Windows (NT): system("cls")
                #Mac OS/Linux (UNIX): system("cls")
        system("cls")
        print("Start")
        for self.row in range(self.__number_Of_Disk):
            for self.column in range(self.__length_Alphabet):
                print(self.Disk[self.row][self.column], end=' ')
            print()
        print("Affichage Console..... OK !")

    def read_TXT (self):
        # Lit le fichier input.txt et efface son contenu
        with open('TXT/input.txt', 'w') as input:
            input.write('')
        print("Lecture Fichier..... OK !")

    def write_TXT (self):
        # Écrit la grille dans le fichier input.txt
        with open('TXT/input.txt', 'w') as output:
            for self.row in range(self.__number_Of_Disk):
                for self.column in range(self.__length_Alphabet):
                    output.write(self.Disk[self.row][self.column])
                output.write('\n')
        print("Écriture Fichier..... OK !")

    def read_dictionnaire_TXT (self):
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

Launch = main()
Launch.view_Console()
Launch.read_TXT()
Launch.write_TXT()
dictionnaire = Launch.read_dictionnaire_TXT()
print(dictionnaire[1])