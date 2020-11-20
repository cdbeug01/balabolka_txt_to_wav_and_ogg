from sys import *
import os

###################### Fonctions utilitaires ########################

def is_number(a):
	chiffres = [".", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	nombre_de_points = 0
	a_tmp = (str)(a)

	if (a==""):
		return False
	j = 0
	for i in a_tmp:
		if (i=="-" and j>0):
			return False
		if (i=="."):
			nombre_de_points+=1
		if (nombre_de_points>1):
			return False
		if i not in chiffres:
			return False
		j+=1
	return True

def is_integer(a):
	if (is_number(a)):
		return ("." not in str(a))
	else:
		return False

def entre_entier(phrase):
	cmp = 0
	res = ""
	while (not is_integer(res)):
		if (cmp>0):
			print("\nVeuiller entrer un entier")
		res = input(phrase)
		cmp+=1
	return int(res)

def lecture_fichier (nom_fichier):
        fichier_oo = open(nom_fichier, 'r')
        oo = fichier_oo.read()
        fichier_oo.close()
        return oo

def ecriture_fichier (nom_du_fichier, res_final):
	fic_w = open(nom_du_fichier, 'w')
	fic_w.write(res_final)
	fic_w.close()

def aff_tab(tab):
	if (tab):
		for i in tab:
			print(i)
'''
	Affiche un dictionnaire
'''
def aff_dict(dict):
	if (dict):
		for i in dict:
			print("\n"+i+" : \n")
			aff_tab(dict[i])

################# Fonctions utilitaires principales #################

def remplace_espaces(nom_fichier):
	res = nom_fichier

	res = res.replace(' ', '_')

	return res

def remplace_espaces_tab(nom_fichier_tab):
	res = []
	for i in nom_fichier_tab:
		res.append(remplace_espaces(i))

	return res

'''
	Enlève les accents et les apostrophes
'''
def remplace_accents(nom_fichier):
	res = nom_fichier

	res = res.replace('é', 'e')
	res = res.replace('è', 'e')
	res = res.replace('à', 'a')
	res = res.replace('ù', 'u')
	res = res.replace('ê', 'e')
	res = res.replace('â', 'a')
	res = res.replace('î', 'i')
	res = res.replace('ï', 'i')
	res = res.replace('ç', 'c')

	res = res.replace(' ', '_')

	res = res.replace("'", "_")

	return res

'''
	Enlèves les ./ en doublons dans chemin
'''

def enleve_points_excessifs (chemin):
	i = 0
	res = ""
	nbr_motif = 0
	while (i<len(chemin)):
		motif = chemin[i:i+2]
		if (motif=='./'):
			nbr_motif+=1
			if (nbr_motif<1):
				res+=motif
		else:
			res+=motif
		i+=2
	return res

def fichier_sans_extension(nom_fichier):
	nom_fichier = nom_fichier.replace('./', '')
	res = ""
	for i in nom_fichier:	
		if (i!='.'):
			res+=i
		else:
			return res

def lecture_arguments_ligne_de_commande ():
	erreurs = []

	chemin = argv[1]

	recursif_ou_non = False
	wav_ou_non = False
	vitesse = 1
	timbre = 10

	argv_args = argv[2:]
	if (len(argv_args)>0):
		for i in range(len(argv_args)):
			
			if ('-r' in argv_args[i].lower()):
				recursif_ou_non = True
			if ('-v' in argv_args[i].lower()):
				if (len(argv_args)>i+1):
					if (is_integer(argv_args[i+1])):
						vitesse_tmp = int(argv_args[i+1])
						if (vitesse_tmp>=-10 and vitesse_tmp<=10):
							vitesse = vitesse_tmp
						else:
							erreurs.append("La vitesse doit être comprise entre -10 et 10 inclus")
			if ('-t' in argv_args[i].lower()):
				if (len(argv_args)>i+1):
					if (is_integer(argv_args[i+1])):
						timbre_tmp = int(argv_args[i+1])
						if (timbre_tmp>=-10 and timbre_tmp<=10):
							timbre = timbre_tmp
						else:
							erreurs.append("Le timbre doit être compris entre -10 et 10 inclus")
			if ('-wav' in argv_args[i].lower()):
				wav_ou_non = True

	return (chemin, recursif_ou_non, wav_ou_non, vitesse, timbre, erreurs)

####################### Fonctions principales #######################

###************************** Dossiers ***************************###

'''
	La fonction liste les fichiers et retire ceux qui n'ont pas d'extension.
	Sous linux, ou en présence de fichiers sans extensions,
	ces fichiers seraient alors ajoutés à la solution.
'''
def liste_dossiers(chemin):
	try :
		fichiers = os.listdir(chemin)
	except:
		return
	dossiers = []
	for i in fichiers:
		if '.' not in i:
			chemin_tmp = enleve_points_excessifs(chemin+'/'+i)
			dossiers.append(chemin_tmp)
	return dossiers

'''
	La fonction utilise la barre '\' pour naviguer dans 
	le système de fichiers.
'''
def liste_dossiers_recursif(chemin):
	os.chdir(chemin)
	chemin = "."
	dossiers = liste_dossiers(chemin)
	if (len(dossiers)>0):
		for i in dossiers:
			chemin_suivant = chemin+'/'+i
			dossiers_tmp = liste_dossiers(chemin_suivant)
			if (dossiers_tmp):
				dossiers.extend(dossiers_tmp)
	return dossiers

###************************** Fichiers ***************************###

def liste_fichiers(chemin):
	try:
		fichiers_tmp = os.listdir(chemin)
	except:
		#print(chemin)
		return

	fichiers_txt = []
	fichiers_OGG = []
	fichiers_WAV = []
	for i in fichiers_tmp:
		if '.txt' in i:
			chemin_tmp = enleve_points_excessifs(i)
			fichiers_txt.append(chemin_tmp)

	for i in fichiers_tmp:
		if '.ogg' in i:
			chemin_tmp = enleve_points_excessifs(i)
			fichiers_OGG.append(chemin_tmp)

	for i in fichiers_tmp:
		if '.wav' in i:
			chemin_tmp = enleve_points_excessifs(i)
			fichiers_WAV.append(chemin_tmp)

	fichiers_a_eviter = []
	for i in fichiers_WAV:
		fichiers_a_eviter.append(fichier_sans_extension(i))
	for i in fichiers_OGG:
		fichiers_a_eviter.append(fichier_sans_extension(i))

	for i in fichiers_a_eviter:
		fichier1 = i
		for j in fichiers_txt:
			fichier2 = fichier_sans_extension(j)
			if (fichier1==fichier2):
				fichiers_txt.remove(j)

	return (fichiers_txt)

def liste_fichiers_recursif(chemin):
	os.chdir(chemin)
	chemin = "."
	dossiers = liste_dossiers_recursif(chemin)
	dossiers.insert(0, '.')

	fichiers = {}
	for i in dossiers:
		fichiers_tab = liste_fichiers(chemin+'/'+i)
		#print(i)
		#aff_tab(fichiers_tab)
		if (fichiers_tab):
			fichiers[i] = fichiers_tab

	return fichiers

###************************ Création BAT *************************###

def balcon (chemin, vitesse, timbre, recursif_ou_non, wav_ou_non):
	chemin_tmp = chemin
	if (recursif_ou_non):
		fichiers = liste_fichiers_recursif(chemin)
	else:
		fichiers = liste_fichiers(chemin)
	if (recursif_ou_non):
		dossiers = []
		for i in fichiers:
			dossiers.append(i)
	else:
		dossiers = ['.']
	nombre_fichier = 0
	if (recursif_ou_non):
		for i in fichiers:
			nombre_fichier+=len(fichiers[i])
	else:
		if (fichiers):
			nombre_fichier = len(fichiers)
		else:
			return

	print("\nListe des fichiers à convertir :")
	if (recursif_ou_non):
		aff_dict(fichiers)
	else:
		print()
		aff_tab(fichiers)
	print("\n")
	print("Choix des options :\n")
	print("- wav_ou_non : "+str(wav_ou_non))
	if (wav_ou_non):
		print("\tLes fichiers seront convertits en .wav uniquement")
	else:
		print("\tLes fichiers seront convertits en .wav, puis en .ogg et les fichiers .wav seront ensuite supprimés")
	print("- recursif_ou_non : "+str(recursif_ou_non))
	if (recursif_ou_non):
		print('\tLes fichiers seront convertits recursivement à partir du chemin "'+chemin+'"')
	else:
		print('\tSeuls les fichers présent dans ce dossier seront convertits : "'+chemin+'"')

	fichier_en_cours_traitement = 0
	print()
	if (recursif_ou_non):
		for i in dossiers:
			if (i=='.'):
				chemin_tmp = chemin
			else:
				chemin_tmp = chemin+"\\"+i
	
			os.chdir(chemin_tmp)
			print('cd "'+chemin+'"\n')
				
			for j in fichiers[i]:
				fichier_en_cours_traitement = balcon_aux(j, vitesse, timbre, wav_ou_non, fichier_en_cours_traitement, nombre_fichier)
	# option non-récursif
	else:
		os.chdir(chemin)
		for i in fichiers:
			fichier_en_cours_traitement = balcon_aux(i, vitesse, timbre, wav_ou_non, fichier_en_cours_traitement, nombre_fichier)

def balcon_aux(nom_fichier, vitesse, timbre, wav_ou_non, fichier_en_cours_traitement, nombre_fichier):
	fichier_en_cours_traitement+=1

	print("Fichier en cours de traitement : "+str(fichier_en_cours_traitement)+"/"+str(nombre_fichier))
	nom_fichier_final_wav = nom_fichier[:len(nom_fichier)-3]+"wav"
	nom_fichier_final_ogg = nom_fichier[:len(nom_fichier)-3]+"ogg"
	commande1 = 'balcon -f "'+nom_fichier+'" -n Virginie_Dri40_16kHz -s '+str(vitesse)+' -p '+str(timbre)+' -v 100 -w "'+nom_fichier_final_wav+'"'
	if (not wav_ou_non):
		commande2 = 'oggenc2 --ignorelength -o "'+nom_fichier_final_ogg+'" "'+nom_fichier_final_wav+'"'
		commande3 = 'del /q "'+nom_fichier_final_wav+'"'

	print('Traitement du fichier "'+nom_fichier+'" :')
	print("Conversion en .wav")
	#print(commande1)
	os.system(commande1)
	print("Fait")
	if (not wav_ou_non):
		print("Conversion en .ogg")
		#print(commande2)
		os.system(commande2)
		print("Suppression du fichier .wav")
		#print(commande3)
		os.system(commande3)
		print("Fait")
	print()

	return fichier_en_cours_traitement

def renomme_dossiers_aux(chemin_depart):
	print("chemin_depart =", chemin_depart)
	os.chdir(chemin_depart)
	chemin = "."

	dossiers = liste_dossiers(chemin)
	for i in dossiers:
		commande = 'ren "'+i+'" '+remplace_accents(i)
		print(commande)
		os.system(commande)
	dossiers = liste_dossiers(chemin)
	for i in dossiers:
		renomme_dossiers_aux(chemin_depart+"\\"+i)

def renomme_dossiers(chemin):
	q = 0
	while (q<1 or q>2):
		print("\nÊtes-vous sûr que vous voulez renommer récursivement les dossiers du chemin : "+chemin+" ?\n\n1 : Oui\n2 : Non")
		q = entre_entier("? = ")
	
	if (q==2): return

	renomme_dossiers_aux(chemin)

def renomme_fichiers (chemin):
	q = 0
	while (q<1 or q>2):
		print("\nÊtes-vous sûr que vous voulez renommer récursivement les dossiers du chemin : "+chemin+" ?\n\n1 : Oui\n2 : Non")
		q = entre_entier("? = ")
	
	if (q==2): return

	dossiers = liste_dossiers_recursif(chemin)
	dossiers.insert(0, '.')
	fichiers = liste_fichiers_recursif(chemin)

	for i in dossiers:
		if (i=='.'):
			os.chdir(chemin)
		else:
			os.chdir(chemin+"\\"+i)
			
		for j in fichiers[i]:
			commande = 'ren "'+j+'" '+remplace_accents(j)
			print(commande)
			os.system(commande)

############################## Tests ################################

def tests():
	#test1()
	#test2()
	#test3()

	return

def test1():
	str1 = "./././././Dossier/Dossier1/Dossier2/Dossier_4"
	print("len(str1) =", len(str1))
	print(str1)
	print(enleve_points_excessifs(str1))

def test2():
	print(fichier_sans_extension("aa1.txt"))
	print(fichier_sans_extension("aa1.wav"))

'''
	Test du renommage de dossiers et de fichier avec confirmation 
	de la part de l'utilisateur.
'''
def test3():
	renomme_dossiers(chemin)
	renomme_fichiers(chemin)

############################### Main ################################

def main ():
	# Erreur lors de la lecture des arguments en ligne de commande
	nombre_arguments_ok = True
	if (len(argv)<2):
		nombre_arguments_ok = False
	else:
		if (len(argv[1])==0):
			nombre_arguments_ok = False

	if (not nombre_arguments_ok):
		print("usage : prgm chemin <arguments>")
		print("\nArguments potentiels :")
		print("\t-r : récursif")
		print("\t-wav ne convertit pas en .ogg, mais seulement en .wav (contertit en .wav, puis en .ogg (avec suppression des .wav par la suite) par défaut)\n")
		print("\t-t (entre -10 et 10 inclus) : timbre de la voix")
		print("\t-v (entre -10 et 10 inclus) : vitesse de la voix")
		exit(1)

	(chemin, recursif_ou_non, wav_ou_non, vitesse, timbre, erreurs) = lecture_arguments_ligne_de_commande()
	if (len(erreurs)>0):
		print("")
		for i in erreurs:
			print(i)
		exit(1)

	#print("timbre =", timbre)
	#print("vitesse =", vitesse)

	#print("chemin =", chemin)
	balcon (chemin, vitesse, timbre, recursif_ou_non, wav_ou_non)

#tests()
main()
