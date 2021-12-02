import os

path = os.getcwd()

## Fonction retournant le chemin vers un fichier.
def getPath(fileName):
	return "{}/{}".format(path, fileName);

## Constantes représentants les touches à appuyer lors de la sélection du « hack »
DICTIONNARY_KEY = "1"
BRUTE_FORCE_KEY = "2"

## Constantes représentants les différents noms de fichier utiles au programme.
DICTIONNARY_HACK_FILE_NAME	= "secret_dictionnary.zip"
BRUTE_FORCE_FILE_NAME		= "secret_bruteforce.zip"
DICTIONNARY_FILE_NAME		= "rockyou.txt"

## Constantes représentants le chemin vers les différents fichiers utiles au programme
DICTIONNARY_HACK_FILE_PATH	= getPath(DICTIONNARY_HACK_FILE_NAME)
BRUTE_FORCE_FILE_PATH		= getPath(BRUTE_FORCE_FILE_NAME)
DICTIONNARY_FILE_PATH		= getPath(DICTIONNARY_FILE_NAME)

## Constantes représentants les messages afficher à la console pour l'utilisateur.
DICTIONNARY_MESSAGE = "{} -> Attaque du dictionnaire sur le fichier « {} »"	.format(DICTIONNARY_KEY, DICTIONNARY_HACK_FILE_NAME)
BRUTE_FORCE_MESSAGE = "{} -> Attaque de brute force sur le fichier  « {} »"	.format(BRUTE_FORCE_KEY, BRUTE_FORCE_FILE_NAME)
ERROR_IN_CHOICE_MESSAGE = "Votre choix est invalide."

## Les différents caractères utile pour la brute force. 
## Pour une expérience complète, ajouté différents caractères spéciaux. Ex: &*/
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

## Le maximum de caractères que la brute force testera. À noter que ce nombre est exclusif.
MAX_BRUTE_FORCE_RANGE = 5

