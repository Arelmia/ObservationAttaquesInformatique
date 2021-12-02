from urllib.request import urlopen, hashlib
from zipfile import ZipFile
import constants
import os
from time import sleep
import sys
import time
import multiprocessing
import itertools

## Cette fonction sert à l'affichage du barre de progrès utilisé lors d'une boucle « for ».
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

## Cette fonction sert à l'affichage d'un ou plusieurs messages à la console.
def showMessages(*messages):
	for message in messages:
		print(message);

## Cette fonction sert à la vérifier le choix de l'utilisateur.
def verifyUserChoice(choice):
	if choice is constants.DICTIONNARY_KEY:
		dictionnaryHack()
	elif choice is constants.BRUTE_FORCE_KEY:
		bruteForce()
	else:
		showMessages(constants.ERROR_IN_CHOICE_MESSAGE)
		main()

## Cette fonction sert à extraire un fichier zip selon son chemin d'accès et un mot de passe.
def unzip(pathToZip, password):
	try:
		ZipFile(pathToZip).extractall(pwd = bytes(password.rstrip(), 'utf-8'))
	except:
		return False
	else:
		return True

## Cette fonction retourne le dictionnaire de mots de passe.
def getDictionnary():
	with open(constants.DICTIONNARY_FILE_PATH , encoding='cp437') as f:
		return f.readlines()

## Cette fonction sert à démarrer le « hack » selon le dictionnaire de mots de passe.
def dictionnaryHack():
	dictionnary = getDictionnary()
	file = constants.DICTIONNARY_FILE_PATH	
	for i in progressbar(range(len(dictionnary)), "Computing: ", 40):
		password = dictionnary[i]
		if unzip(file, password):
			sys.stdout.write("\n")
			print("The password is {}".format(password), end=" ")
			return

## Cette fonction retourne toutes les combinaisons de lettres selon une certaines longueurs.
def getCombinaisons(lenght):
	return [''.join(i) for i in itertools.product(constants.ALPHABET, repeat = lenght)]

## Cette fonction sert à démarrer le « hack » selon la méthode « bruteForce »
def bruteForce():
	file = constants.BRUTE_FORCE_FILE_PATH	
	allCombinaisons = []
	for i in 	progressbar(range(constants.MAX_BRUTE_FORCE_RANGE), "Preparing the work... ", 40):
		allCombinaisons = allCombinaisons+getCombinaisons(i)

	for i in progressbar(range(len(allCombinaisons)), "Computing: ", 40):
		password = allCombinaisons[i]
		
		sys.stdout.write("Trying password: {}  | ".format(password))

		if unzip(file, password):
			sys.stdout.write("\n")
			print("The password is {}".format(password), end=" ")
			return

## Cette fonction sert à démarrer l'application.
def main():
	showMessages(constants.DICTIONNARY_MESSAGE, constants.BRUTE_FORCE_MESSAGE)
	verifyUserChoice(input())

main()

# Technique du dictionnaire:
#	Facile à coder,
#	Long à parcourir tout les mots de passes (Moins que la technique brute force, mais quand même)
#	Peu efficace contre des mots de passes plus rechercher.
# Technique brute force
#	Difficile à coder
#	Extrêmement long de parcourir toutes les possibilités
#	Incomplète, puisque ça ne comprend pas les charactères spéciaux
#	Tue à petit feu notre mac 2019
# Lequel que j'ai le plus aimé
#	La technique brute force était cool à réaliser, bien que d'un niveau performance sur un seul ordinateur,
#	la technique du dictionnaire resterais mieux. De plus, ça atteindrais plus les gens qui ne 
#	s'y connaisse pas en informatique, donc un publique cible pour les hacker moderne.
#	Pour une meilleur comparaison, je propose d'améliorer la brute force et d'utiliser plusieurs ordinateurs
