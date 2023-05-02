import math
from os import system
import tkinter
import random

class main:
    def __init__(self):
        #Initialise les valeurs 
        self.__alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.__length_Alphabet = len(self.__alphabet)
        self.__number_Of_Disk = 26
        self.__length_Of_Disk = self.__length_Alphabet
        self.Disk = [self.__alphabet] * self.__number_Of_Disk
        self.row = 0
        self.column = 0

    def view(self):
        #Affichage console du cylindre 
        system("cls")
        print("Start")
        for self.row in range(self.__number_Of_Disk):
            for self.column in range(self.__length_Alphabet):
                print(self.Disk[self.row][self.column], end=' ')
            print()
        print("Affichage Console..... OK !")

    def read_TXT (self):
        #Lit le fichier input.txt et efface son contenu
        with open('TXT/input.txt', 'w') as input:
            input.write('')
        print("Lecture Fichier..... OK !")

    def write_TXT (self):
        #Écrit la grille dans le fichier input.txt
        with open('TXT/input.txt', 'w') as output:
            for self.row in range(self.__number_Of_Disk):
                for self.column in range(self.__length_Alphabet):
                    output.write(self.Disk[self.row][self.column])
                output.write('\n')
        print("Écriture Fichier..... OK !")

Launch = main();
Launch.view();
Launch.read_TXT();
Launch.write_TXT();


#class view : 
#class read_TXT :    
#class write_TXT :