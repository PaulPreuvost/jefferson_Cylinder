from os import system
import tkinter as tk
import random


class JeffersonCylinder:
    def __init__(self, init_fichier: str, init_n: int):
        self.key = []  # Liste vide pour stocker la clé
        self.fichier = init_fichier  # Nom du fichier
        self.n = init_n  # Nombre de lignes du cylindre
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                         "T", "U", "V", "W", "X", "Y", "Z"]  # Liste des lettres de l'alphabet
        self.length_alphabet = len(self.alphabet)  # Longueur de l'alphabet
        self.permutation = [None] * self.length_alphabet  # Liste de permutation initialisée avec des valeurs None
        self.disk = []  # Liste pour stocker la grille du cylindre
        self.dictionnaire = {}  # Dictionnaire
        self.row = 0  # Ligne courante
        self.column = 0  # Colonne courante

    def grid_creation(self):
        # Ajoute l'alphabet dans un ordre différent à chaque ligne en ajoutant dans le self.disk
        for i in range(self.n):
            temp = self.alphabet.copy()  # Copie de l'alphabet
            random.shuffle(temp)  # Mélange aléatoire des lettres
            self.disk.append(temp)  # Ajout de la ligne mélangée à la grille du cylindre

    def view_console(self):
        # Affichage console du cylindre
        # La prochaine ligne permet de "clear" le terminal:
        # Windows (NT): system("cls")
        # Mac OS/Linux (UNIX): system("clear")
        system("cls")  # Effacement de la console
        print("Start")
        for self.row in range(self.n):  # Parcours des lignes
            for self.column in range(self.length_alphabet):  # Parcours des colonnes
                print(self.disk[self.row][self.column], end=' ')  # Affichage de la lettre
            print()  # Nouvelle ligne
        print("Affichage Console..... OK !")  # Message de confirmation

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

    def verif_key(self, text):
        # Vérifie si la clé est valide pour le texte donné
        key_length = len(self.key)
        key_set = set(self.key)

        if len(key_set) != key_length and key_length != len(text):
            return False

        if key_length < self.n:
            return False

        for number in self.key:
            if number <= 0 or number > len(self.dictionnaire):
                return False

        return True

    def generate_permutation_key(self):
        # Génère une permutation aléatoire de la clé
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

        # Récupérer la position de la lettre qu'on veut crypter dans le dictionnaire
        letter_position = dictionnaire.index(letter)

        # Récupérer la 6e lettre après celle qu'on veut crypter dans le dictionnaire
        decrypted_position = (letter_position - 6) % len(dictionnaire)
        decrypted_letter = dictionnaire[decrypted_position]

        self.column += 1  # Mettre à jour l'index de colonne
        return decrypted_letter

    def encrypt_text(self, text):
        self.remove(text)  # Supprimer les caractères indésirables du texte
        if self.verif_text(text) and self.verif_key(text):
            encrypted_text = ""  # Variable pour stocker le texte crypté
            key_length = len(self.key)  # Longueur de la clé de cryptage

            for i, letter in enumerate(text):
                # Obtenir le dictionnaire correspondant à l'index de la clé actuelle + 1
                dictionnaire = self.dictionnaire[self.key[i % key_length]]

                # Convertir la lettre en majuscule
                letter = letter.upper()

                # Crypter la lettre en utilisant la fonction encrypt_letter
                encrypted_letter = self.encrypt_letter(letter, dictionnaire)

                # Ajouter la lettre cryptée au texte crypté
                encrypted_text += encrypted_letter

            return encrypted_text  # Renvoyer le texte crypté
        else:
            erreur = "Problème de taille ou de clé"  # Message d'erreur en cas de problème
            return erreur

    def decrypt_text(self, text):
        self.remove(text)  # Supprimer les caractères indésirables du texte
        if self.verif_text(text) and self.verif_key(text):
            decrypted_text = ""  # Variable pour stocker le texte décrypté
            key_length = len(self.key)  # Longueur de la clé de décryptage

            for i, letter in enumerate(text):
                # Obtenir le dictionnaire correspondant à l'index de la clé actuelle
                dictionnaire = self.dictionnaire[self.key[i % key_length]]

                # Convertir la lettre en majuscule
                letter = letter.upper()

                # Décrypter la lettre en utilisant la fonction decrypt_letter
                decrypted_letter = self.decrypt_letter(letter, dictionnaire)

                # Ajouter la lettre décryptée au texte décrypté
                decrypted_text += decrypted_letter

            return decrypted_text  # Renvoyer le texte décrypté
        else:
            erreur = "Problème de taille ou de clé"  # Message d'erreur en cas de problème
            return erreur


class Graphique:

    def __init__(self):
        # Initialisation de la fenêtre principale
        self.window = tk.Tk()
        self.window.title("Cylindre de Jefferson")  # Titre de la fenêtre
        self.window.configure(background='white')  # Couleur de fond de la fenêtre
        self.window.geometry("800x800")  # Dimensions de la fenêtre

        # Configuration de l'icône de la fenêtre
        self.window.iconbitmap("images/icone.ico")

        # Label pour afficher le texte "Taille de votre phrase/mot"
        self.size_label = tk.Label(self.window, text="Taille de votre phrase/mot", font=("Helvetica", 14),
                                   bg="white")
        self.size_label.pack()

        # Zone de saisie pour entrer la taille de la phrase/mot
        self.size_entry = tk.Entry(self.window, width=40)
        self.size_entry.pack()
        self.size_entry.bind("<KeyRelease>", self.update_size_entry)  # Lien avec la méthode update_size_entry
        self.size_entry_value = ""  # Variable pour stocker la valeur du widget

        # Bouton "Generate" pour générer le résultat
        self.generate_button = tk.Button(self.window, text="Generate", width=10, command=self.generate)
        self.generate_button.pack(padx=5)

        # Label pour afficher le cylindre de Jefferson
        self.label = tk.Label(self.window, text=self.display_cylindre(test_cylinder), font=("Helvetica", 16),
                              bg="white")
        self.label.pack(pady=20)

        # Frame pour les boutons de sélection de clé
        self.frame = tk.Frame(self.window, bg="white")
        self.frame.pack()

        # Boucle pour créer les boutons de sélection de clé
        for i in range(1, len(test_cylinder.dictionnaire) + 1):
            button = tk.Button(self.frame, text=str(i), width=5, height=2, command=lambda i=i: self.add_key(i))
            button.pack(side=tk.LEFT, padx=5, pady=5)

        # Label pour afficher le texte "KEY"
        self.key_label = tk.Label(self.window, text="KEY", font=("Helvetica", 14), bg="white")
        self.key_label.pack(pady=10)

        # Frame pour le chiffrement du texte
        self.encrypt_frame = tk.Frame(self.window, bg="white")
        self.encrypt_frame.pack()

        vcmd = (self.window.register(lambda text: "-" not in text and " " not in text), '%P')

        # Zone de saisie pour le texte à crypter
        self.text_encrypt = tk.Entry(self.encrypt_frame, width=40, validate="key", validatecommand=vcmd)
        self.text_encrypt.pack(side=tk.LEFT)

        # Bouton "Crypter" pour chiffrer le texte
        self.crypt_button = tk.Button(self.encrypt_frame, text="Chiffrer", width=10, command=self.encrypt)
        self.crypt_button.pack(side=tk.LEFT, padx=5)

        # Frame pour le déchiffrement du texte
        self.decrypt_frame = tk.Frame(self.window, bg="white")
        self.decrypt_frame.pack()

        # Zone de saisie pour le texte à décrypter
        self.text_decrypt = tk.Entry(self.decrypt_frame, width=40, validate="key", validatecommand=vcmd)
        self.text_decrypt.pack(side=tk.LEFT)

        # Bouton "Décrypter" pour décrypter le texte
        self.decrypt_button = tk.Button(self.decrypt_frame, text="Déchiffrer", width=10, command=self.decrypt)
        self.decrypt_button.pack(side=tk.LEFT, padx=5)

        # Label pour afficher le résultat
        self.result_label = tk.Label(self.window, text="RESULT", font=("Helvetica", 14), bg="white")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(self.window, text="Reset", width=10, command=self.reset)
        self.reset_button.pack()

    def update_size_entry(self, event):
        # Met à jour la valeur de self.size_entry_value en utilisant la valeur actuelle de self.size_entry
        self.size_entry_value = self.size_entry.get()

    def display_cylindre(self, cylindres):
        cylindre = ""
        # Parcours chaque élément du dictionnaire test_cylinder.dictionnaire
        for i in range(1, len(cylindres.dictionnaire) + 1):
            # Ajoute la valeur du cylindre correspondant à l'indice i au texte cylindre
            cylindre += cylindres.dictionnaire[i]
            cylindre += "\n"  # Ajoute un saut de ligne à la fin de chaque cylindre
        return cylindre  # Retourne le texte des cylindres

    def add_key(self, n):
        # Vérifie si n n'est pas déjà présent dans la liste des clés test_cylinder.key
        if n not in test_cylinder.key:
            # Ajoute n à la liste des clés test_cylinder.key
            test_cylinder.key.append(n)
            # Met à jour le texte de self.key_label en utilisant la méthode display_key()
            self.key_label.config(text=self.display_key())

    def display_key(self):
        key = ""
        # Parcours chaque élément de la liste des clés test_cylinder.key
        for i in range(len(test_cylinder.key)):
            # Ajoute la clé actuelle convertie en chaîne de caractères à la variable key
            key += str(test_cylinder.key[i])
            key += "  "  # Ajoute deux espaces après chaque clé
        return key  # Retourne le texte des clés

    def encrypt(self):
        text = self.text_encrypt.get()
        # Vérifie si la liste des clés test_cylinder.key est identique à test_cylinder.n
        if len(test_cylinder.key) == len(text):
            # Récupère le texte à chiffrer à partir de self.text_encrypt
            # Appelle la méthode encrypt_text() de test_cylinder pour chiffrer le texte
            encryptedText = test_cylinder.encrypt_text(text)
            # Met à jour le texte de self.result_label avec le texte chiffré
            self.result_label.config(text=encryptedText)
        else:
            # Si la taille de la clé est différente du nombre de cylindres, retourne un message d'erreur
            error = "La taille de la clé doit être identique au nombre de cylindre"
            self.result_label.config(text=error)

    def decrypt(self):
        text = self.text_decrypt.get()  # Récupère le texte à décrypter depuis l'interface
        # Vérifie si la clé est égale au nombre de cylindres
        if len(test_cylinder.key) == len(text):
            decryptedText = test_cylinder.decrypt_text(
                text)  # Décrypte le texte en utilisant la méthode decrypt_text du test_cylinder
            self.result_label.config(text=decryptedText)  # Affiche le texte décrypté dans l'interface
        else:
            error = "La taille de la clé doit être identique au nombre de cylindre"
            return error

    def reset(self):
        # Réinitialise la clé du test_cylinder
        test_cylinder.key = []
        # Met à jour l'étiquette de la clé affichée
        self.key_label.config(text="KEY")
        # Réinitialise le label de résultat
        self.result_label.config(text="RESULT")

    def destroy(self):
        self.window.destroy()  # Détruit la fenêtre de l'interface

    def generate(self):
        out = self.size_entry.get()  # Récupère la valeur saisie dans self.size_entry
        number = int(out)  # Convertit la valeur en entier
        self.destroy()  # Détruit la fenêtre de l'interface actuelle
        del test_cylinder.dictionnaire
        test_cylinder2 = JeffersonCylinder('txt/input.txt',
                                           number)  # Crée une nouvelle instance de la classe JeffersonCylinder avec
        # le fichier 'txt/input.txt'
        # et le nombre de cylindres spécifié
        test_cylinder2.grid_creation()  # Crée la grille des cylindres
        test_cylinder2.read_TXT()  # Lit le contenu du fichier texte
        test_cylinder2.write_TXT()  # Écrit le contenu des cylindres dans le fichier texte
        test_cylinder2.read_dictionnaire_TXT()  # Lit le dictionnaire à partir du fichier texte
        graphique2 = Graphique()  # Crée une instance de la classe Graphique
        graphique2.run()  # Lance la méthode run de l'instance de la classe Graphique
        self.label.config(text=self.display_cylindre(test_cylinder2))
        print("generate")

    def run(self):
        self.window.mainloop()  # Lance la boucle principale de l'interface

    # Exemple d'utilisation


if __name__ == "__main__":
    test_cylinder = JeffersonCylinder('txt/input.txt',
                                      6)  # Crée une instance de la classe JeffersonCylinder avec le fichier
    # 'txt/input.txt' et 6 cylindres
    test_cylinder.grid_creation()  # Crée la grille des cylindres
    test_cylinder.read_TXT()  # Lit le contenu du fichier texte
    test_cylinder.write_TXT()  # Écrit le contenu des cylindres dans le fichier texte
    test_cylinder.read_dictionnaire_TXT()  # Lit le dictionnaire à partir du fichier texte
    graphique = Graphique()  # Crée une instance de la classe Graphique
    graphique.run()  # Lance la méthode run de l'instance de la classe Graphique
