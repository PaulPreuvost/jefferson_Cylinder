import math
from os import system
import tkinter as tk
import random


class main:
    def __init__(self, init_key: list, init_fichier: str):
        self.key = init_key
        self.fichier = init_fichier
        self.n = len(self.key)
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
        with open(self.fichier, 'w') as input:
            input.write('')
        print("Lecture Fichier..... OK !")

    def write_TXT(self):
        # Écrit la grille dans le fichier input.txt
        with open(self.fichier, 'w') as output:
            for self.row in range(self.n):
                for self.column in range(self.length_alphabet):
                    output.write(self.disk[self.row][self.column])
                output.write('\n')
        print("Écriture Fichier..... OK !")

    def read_dictionnaire_TXT(self):
        # Lit le fichier input.txt et crée un dictionnaire
        self.dictionnaire = {}
        with open(self.fichier, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                # Supprime les caractères en trop
                line = line.strip()
                # Ajoute la ligne dans le dictionnaire avec la clé correspondante (index 1 à 26)
                self.dictionnaire[i + 1] = line
        print("Enregistrement Dictionnaire..... OK !")
        return self.dictionnaire

    def verif_key(self):
        key_length = len(self.key)
        key_set = set(self.key)

        if len(key_set) != key_length:
            return False

        for number in self.key:
            if number <= 0 or number > key_length:
                return False

        return True

    def generate_permutation_key(self):
        random.shuffle(self.key)
        return self.key

    def generate_permutation(self):
        shifted_permutation = list(range(26))
        self.permutation = shifted_permutation[6:] + shifted_permutation[:6]
        return self.permutation

    def verif_text(self, text):
        key_length = len(self.key)

        text_without_spaces = text.replace(" ", "").replace("-", "")

        if len(text_without_spaces) != key_length:
            return False
        else:
            return True

    def remove(self, text):
        return text.replace(" ", "").replace("-", "")

    def encrypt_letter(self, letter, dictionnaire):
        if letter == ' ':
            return ' '

        index = self.alphabet.index(letter.upper())  # Convertir la lettre en majuscule
        key_index = self.key[self.column % self.n] - 1  # Index de la clé pour la colonne actuelle
        cipher_index = self.permutation[(index + key_index) % self.length_alphabet]

        # Récupérer la lettre chiffrée correspondant à cipher_index
        cipher_letter = self.alphabet[cipher_index]

        # Récupérer la position de la lettre qu'on veut crypter dans le dictionnaire
        letter_position = dictionnaire.index(letter)

        # Récupérer la 6e lettre après celle qu'on veut crypter dans le dictionnaire
        encrypted_position = (letter_position + 6) % len(dictionnaire)
        encrypted_letter = dictionnaire[encrypted_position]

        self.column += 1  # Mettre à jour l'index de colonne
        return encrypted_letter

    def decrypt_letter(self, letter, dictionnaire):
        if letter == ' ':
            return ' '

        index = self.alphabet.index(letter.upper())  # Convertir la lettre en majuscule
        key_index = self.key[self.column % self.n] - 1  # Index de la clé pour la colonne actuelle
        cipher_index = self.permutation[(index + key_index) % self.length_alphabet]

        # Récupérer la lettre chiffrée correspondant à cipher_index
        cipher_letter = self.alphabet[cipher_index]

        # Récupérer la position de la lettre qu'on veut crypter dans le dictionnaire
        letter_position = dictionnaire.index(letter)

        # Récupérer la 6e lettre après celle qu'on veut crypter dans le dictionnaire
        decrypted_position = (letter_position - 6) % len(dictionnaire)
        decrypted_letter = dictionnaire[decrypted_position]

        self.column += 1  # Mettre à jour l'index de colonne
        return decrypted_letter

    def encrypt_text(self, text):
        if self.verif_text(text) and self.verif_key():
            encrypted_text = ""
            key_length = len(self.key)

            for i, letter in enumerate(text):
                # Obtenir le dictionnaire correspondant à l'index de la clé actuelle + 1
                dictionnaire = self.dictionnaire[self.key[i % key_length]]

                # Convertir la lettre en majuscule
                letter = letter.upper()

                # Crypter la lettre en utilisant la fonction encrypt_letter
                encrypted_letter = self.encrypt_letter(letter, dictionnaire)

                # Ajouter la lettre cryptée au texte crypté
                encrypted_text += encrypted_letter

            return encrypted_text
        else:
            erreur = "Problème de taille ou de clé"
            return erreur

    def decrypt_text(self, text):
        if self.verif_text(text) and self.verif_key():
            decrypted_text = ""
            key_length = len(self.key)

            for i, letter in enumerate(text):
                # Obtenir le dictionnaire correspondant à l'index de la clé actuelle
                dictionnaire = self.dictionnaire[self.key[i % key_length]]

                # Convertir la lettre en majuscule
                letter = letter.upper()

                # Décrypter la lettre en utilisant la fonction decrypt_letter
                decrypted_letter = self.decrypt_letter(letter, dictionnaire)

                # Ajouter la lettre décryptée au texte décrypté
                decrypted_text += decrypted_letter

            return decrypted_text
        else:
            erreur = "Problème de taille ou de clé"
            return erreur


test_cylinder = main([7,9,5,10,1,6,3,8,2,4], 'txt/cylinderWiki.txt')
#test_cylinder.grid_creation()
#test_cylinder.read_TXT()
#test_cylinder.write_TXT()
test_cylinder.read_dictionnaire_TXT()

print(f'La 1 ligne du dictionnaire est : {test_cylinder.dictionnaire[1]}')
print(f'La 2 ligne du dictionnaire est : {test_cylinder.dictionnaire[2]}')
print(f'La 3 ligne du dictionnaire est : {test_cylinder.dictionnaire[3]}')
print(f'La 4 ligne du dictionnaire est : {test_cylinder.dictionnaire[4]}')
print(f'La 5 ligne du dictionnaire est : {test_cylinder.dictionnaire[5]}')
print(f'La 6 ligne du dictionnaire est : {test_cylinder.dictionnaire[6]}')
test_cylinder.generate_permutation()

print(test_cylinder.key)
texte = test_cylinder.remove("Retreat Now")
test = test_cylinder.encrypt_text(texte)
print(test)
test2 = test_cylinder.decrypt_text(test)
print(test2)

# POur le graphique
# Appeler le dictionnaire pour afficher les cylindres
# Les mettre à la verticale
# Faires input avec boutons pour appeler les fonctions crypter et décrypter
# CHercher un sytème pour selectionner une clé
