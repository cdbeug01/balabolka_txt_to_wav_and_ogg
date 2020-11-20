# balabolka_txt_to_wav_and_ogg
Can convert several files of txt (format ANSI (it is named like it on notepad.exe)) to WAV and OGG using Balabolka and Oggenc2

(All is in French)

Le programme peut convertir plusieurs fichiers en un coup, à condition qu'il soient placés dans un même dossier. Inclue la récursivité.
Plus d'information dans le fichier READ-ME.txt

____

A Exécuter avec Python3.

Il faut avoir téléchargé et installé dans le path (cf : http://sametmax.com/ajouter-un-chemin-a-la-variable-denvironnement-path-sous-windows/ )  balabolka (cf : http://www.cross-plus-a.com/balabolka.htm , voir "Command Line Utility") et oggenc2 (cf : https://www.rarewares.org/ogg-oggenc.php ) et Python3.

Pour installer python3, rendez-vous sur cette page https://www.python.org/downloads/

Le but du programme est d'automatiser la conversion de plusieurs fichiers .txt à la fois, ce qui n'est pas possible avec la version avec interface graphique de Balabolka : (disponible ici ) http://www.cross-plus-a.com/fr/balabolka.htm

___

Disclamers : 

Le présent code n'est pas parfait. Le principe d'un bon travail en coding est de s'améliorer en itérant (en améliorant chaque fois un petit peu, par touche ce qui peut l'être)
Je ne dispose que de très peu de temps pour coder. Je fais cela sur mon temps libre.

Les liens donnés était viables au moment de l'écriture de ces lignes (et ne le seront peut-être plus par la suite).
Renseignez-vous avant de télécharger des logiciels et de les installer. Les sites donnés le sont à titre indicatif. Je ne garantit rien vis-à-vis de leur fiabilité, ni concernant la fiabilité de mon programme.

Le programme est fait pour Fonctionner sous Windows.

Pour l'allumer, faîtes Menu démarrer, chercher l'invité de commandes (ou "cmd"), puis tapez "cd " suivie de l'adresse d'où se trouve le fichier "balabolka_txt.py" (voir dans la barre d'adresse de l'explorateur de fichiers). Puis tapez "cls&&python3 balabolka_txt.py", suivi de l'adresse de là où se trouvent les fichier à convertir.
Des options peuvent être ajoutée dans la commande (voir le fichier READ-ME)

____

Exemples de commandes : 

python3 balabolka_txt.py -r "C:\Users\Nom_Utilisateur\Dossier_contenant_les_fichiers_a_convertir"

python3 balabolka_txt.py -v 2 "C:\Users\Nom_Utilisateur\Dossier_contenant_les_fichiers_a_convertir"

python3 balabolka_txt.py -v -r 2 "C:\Users\Nom_Utilisateur\Dossier_contenant_les_fichiers_a_convertir"


Le programme a été testé uniquement sous Windows 7 en 2019 et 2020.
