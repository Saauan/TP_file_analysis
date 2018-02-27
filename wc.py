"""
Script Python permettant de calculer le nombre de lignes, de mots et de caractères d'un fichier texte ou d'un input utilisateur
Usage : wc.py [OPTION] [ENCODAGE] [<nom fichier>]
        <nom fichier> = nom du fichier (texte) à examiner. Si absent : stdin (input utilisateur)
        <encodage> = encodage à utiliser pour lire le texte. Si absent : utf-8
        OPTION =
                -h   : cette aide
                -lw  : nombre de lignes et de mots
                -lwc : nombre de lignes, de mots et de caractères
                -c   : nombre de caractères
                -l   : nombre de lignes
                -wc  : nombre de mots et de caractères
                -w   : nombre de mots
                -lc  : nombre de lignes et de caractères
        Si aucune n'option n'est spécifiée, -lwc est utilisée
        
auteur : Coignion Tristan Becquembois Logan
création: 20/02/2018
dernière révision: 23/02/2018
"""

import string
import sys
import os.path
SEPARATEURS = string.punctuation + "\n \t"

def decoupe_en_mots(s):
    """
    Renvoie la liste des mots contenus dans la chaîne de caractères passée en paramètre
    
    Exemples:
    >>> decoupe_en_mots("Ceci, est un test aujourd\'hui. \t Liorem,")
    ['Ceci', 'est', 'un', 'test', 'aujourd', 'hui', 'Liorem']
    """
    s_separateurs = ""
    for c in s:
        if c in SEPARATEURS:
            c = " "
        s_separateurs += c
    s_separateurs = s_separateurs.split()
    return s_separateurs
    
def analyse(stream):
    """
    Renvoie un triplet (l,m,c) d'entiers indiquant le nombre de lignes, de mots et de caractères lus via le canal entré en paramètre jusqu'à la fin
    
    Exemples:
    >>> with open("cigale.txt","r",encoding="utf-8") as exemple:
    ...   analyse(exemple)
    (24, 114, 624)
    """
    texte_lignes = stream.readlines()
    texte_str = "".join(texte_lignes)
    texte_mots = decoupe_en_mots(texte_str)
    m = len(texte_mots)
    c = len(texte_str)
    l = len(texte_lignes)
    return l,m,c
    
def usage():
    """
    Imprime une aide à l'utilisation du script
    Se termine par l'instuction exit(1) qui provoque l'arrêt de l'éxecution du script en cours
    """
    with open("usage.txt", "r", encoding = "latin-1") as usage:
        for ligne in usage:
            print(ligne, end="")
            

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)


if len(sys.argv) == 2 and sys.argv[1] == "-h":
    usage()

else:
    try:
        option = "-lwc"
        encodage = "utf-8"
        
        if len(sys.argv) >= 2: # Nom de fichier spécifié
            if len(sys.argv) >= 3: # Option + Nom de fichier
                option = sys.argv[1]
                if not option[0] == "-":
                    raise NameError("l'argument [OPTION] doit commencer par un '-'. Pour plus d'informations utiliser '-h'")
                if len(sys.argv) >=4: # Option + Encodage + Nom de fichier
                    encodage = sys.argv[2]
                    fichier = sys.argv[3]
                else:    
                    fichier = sys.argv[2]

            else: # Seulement un nom de fichier
                fichier = sys.argv[1]
            if not os.path.isfile(fichier):
                raise FileNotFoundError("fichier inexistant")
            with open(fichier, 'r', encoding=encodage) as canal_texte:
                l, m, c = analyse(canal_texte)
                
        else: # Si le nom de fichier est non spécifié
            if len(sys.argv) >= 2:
                option = sys.argv[1]
            print("Reading from stdin...")
            print("Press Ctrl + D to end send EOF (Ctrl + Z on Windows)")
            fichier = sys.stdin
            l, m, c = analyse(sys.stdin)
    
        if option == "-lw":
            print(l, m)
        if option == "-lwc":
            print(l, m, c)
        if option == "-c":
            print(c)
        if option == "-l":
            print(l)
        if option == "-wc":
            print(m, c)
        if option == "-w":
            print(m)
        if option == "-lc":
            print(l, c)
                
            
    except NameError as erreur:
        print(erreur)
    except FileNotFoundError as erreur:
        print(erreur)
    except LookupError:
        print("l'encodage utilisé est erroné !")
    