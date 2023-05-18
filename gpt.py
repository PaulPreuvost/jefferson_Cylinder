import math
from os import system
import tkinter
import random

class main:
    def __init__(self, init_key: list, init_n: int, init_texte: str):
        self.key = init_key
        self.n = init_n
        self.texte = init_texte
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.length_alphabet = len(self.alphabet)
        self.permutation = None
        self.disk = []
        self.dictionnaire = None
        self.row = 0
        self.column = 0

    def grid_creation(self):
        # Ajoute l'alphabet dans un ordre différent à chaque ligne en ajoutant dans le self.disk
        for i in range(self.n):
            temp = self.alphabet.copy()
            random.shuffle(temp)
            self.disk.append(temp)

    def view_console(self):
        # Affichage console du cylindre
        # La prochaine ligne permet de "clear" le terminal:
        # Windows (NT): system("cls")
        # Mac OS/Linux (UNIX): system("clear")
        system("cls")
        print("Start")
        for self.row in range(self.n):
            for self.column in range(self.length_alphabet):
                print(self.disk[self.row][self.column], end=' ')
            print()
        print("Affichage Console..... OK !")

    def read_TXT(self):
        # Lit le fichier input.txt et efface son contenu
        with open('txt/input.txt', 'w') as input:
            input.write('')
        print("Lecture Fichier..... OK !")

    def write_TXT(self):
        # Écrit la grille dans le fichier input.txt
        with open('txt/input.txt', 'w') as output:
            for self.row in range(self.n):
                for self.column in range(self.length_alphabet):
                    output.write(self.disk[self.row][self.column])
                output.write('\n')
        print("Écriture Fichier..... OK !")

    def read_dictionnaire_TXT(self):
        # Lit le fichier input.txt et crée un dictionnaire
        self.dictionnaire = {}
        with open('txt/input.txt', 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                # Supprime les caractères en trop
                line = line.strip()
                # Ajoute la ligne dans le dictionnaire avec la clé correspondante (index 1 à 26)
                self.dictionnaire[i+1] = line
        print("Enregistrement Dictionnaire..... OK !")
        return self.dictionnaire

    def verif_permutation_key(self):
        # Vérifie si la clé est une permutation valide des entiers de 1 à n.
        # key (list[int]): Une liste d'entiers représentant la clé.
        # bool: True si la clé est valide, False sinon.
        if len(self.key) == self.n:
            if len(self.key) != len(set(self.key)):
                # Vérifie si les entiers de la clé sont uniques.
                print("False")
                return False
            if set(self.key) != set(range(1, len(self.key) + 1)):
                # Vérifie si les entiers de la clé sont tous compris entre 1 et n.
                print("False")
                return False
            print("True")
            # Permute aléatoirement les éléments de la liste
            return True
        print("False")
        return False

    def generate_permutation_key(self):
        random.shuffle(self.key)
        return self.key

    def generate_permutation(self):
        shifted_permutation = list(range(26))
        self.permutation = shifted_permutation[6:] + shifted_permutation[:6]
        return self.permutation

    def encrypt_letter(self, letter):
        if letter == ' ':
            return ' '
        index = self.alphabet.index(letter.upper())  # Convertir la lettre en majuscule
        cipher_index = self.permutation[index]
        cipher_letter = self.alphabet[cipher_index]
        return cipher_letter

    def decrypt_letter(self, cipher_letter):
        if cipher_letter == ' ':
            return ' '
        cipher_index = self.alphabet.index(cipher_letter.upper())  # Convertir la lettre en majuscule
        index = self.permutation.index(cipher_index)
        letter = self.alphabet[index]
        return letter

    def encrypt_text(self):
        print(self.texte)
        self.generate_permutation_key()
        self.generate_permutation()
        encrypted_text = ""
        for letter in self.texte:
            encrypted_text += self.encrypt_letter(letter)
        print("Texte chiffré :", encrypted_text)

    def decrypt_text(self, texteD):
        decrypted_text = ""
        for letter in texteD:
            decrypted_text += self.decrypt_letter(letter)
        print("Texte déchiffré :", decrypted_text)


test_cylinder = main([2,4,6,1,5,3], 6, "Manges mes couilles")
test_cylinder.grid_creation()
test_cylinder.view_console()
test_cylinder.read_TXT()
test_cylinder.write_TXT()
test_cylinder.read_dictionnaire_TXT()
test_cylinder.verif_permutation_key()
print(f'Clé avant permutation{test_cylinder.key}')
test_cylinder.generate_permutation_key()
print(f'Clé après permutation{test_cylinder.key}')

print(f'La 1 ligne du dictionnaire est : {test_cylinder.dictionnaire[1]}')
print(f'La 2 ligne du dictionnaire est : {test_cylinder.dictionnaire[2]}')
print(f'La 3 ligne du dictionnaire est : {test_cylinder.dictionnaire[3]}')
print(f'La 4 ligne du dictionnaire est : {test_cylinder.dictionnaire[4]}')
print(f'La 5 ligne du dictionnaire est : {test_cylinder.dictionnaire[5]}')
print(f'La 6 ligne du dictionnaire est : {test_cylinder.dictionnaire[6]}')
test_cylinder.generate_permutation()
print(test_cylinder.encrypt_letter('H'))
print(test_cylinder.decrypt_letter('R'))

print()
test_cylinder.encrypt_text()
test_cylinder.decrypt_text("SGTMKY SKY IUAORRKY")