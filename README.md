# balabolka_txt_to_wav_and_ogg
Can convert several files of txt (format ANSI (it is named like it on notepad.exe)) to WAV and OGG using Balabolka and Oggenc2


Le programme peut convertir plusieurs fichiers en un coup, à condition qu'il soient placés dans un même dossier. Inclue la récursivité.
Plus d'information dans le fichier READ-ME.txt (l'autre READ-ME).

____

A Exécuter avec Python3.


Il faut avoir téléchargé et installé dans le path (cf : http://sametmax.com/ajouter-un-chemin-a-la-variable-denvironnement-path-sous-windows/ )  balabolka (cf : http://www.cross-plus-a.com/balabolka.htm , voir "Command Line Utility") et oggenc2 (cf : https://www.rarewares.org/ogg-oggenc.php ) et Python3.

Pour installer python3, rendez-vous sur cette page : https://www.python.org/downloads/ .

Le but du programme est d'automatiser la conversion de plusieurs fichiers .txt à la fois, ce qui n'est pas possible avec la version avec interface graphique de Balabolka : (disponible ici : http://www.cross-plus-a.com/fr/balabolka.htm ).

___

Disclamers : 


Le présent code n'est pas parfait. Le principe d'un bon travail en coding est de s'améliorer en itérant (en améliorant chaque fois un petit peu, par touche ce qui peut l'être)
Je ne dispose que de très peu de temps pour coder. Je fais cela sur mon temps libre.

Les liens donnés étaient viables au moment de l'écriture de ces lignes (et ne le seront peut-être plus par la suite).
Renseignez-vous avant de télécharger des logiciels et de les installer. Les sites donnés le sont à titre indicatif. Je ne garantis rien vis-à-vis de leur fiabilité, ni concernant la fiabilité de mon programme.

Le programme est fait pour fonctionner sous Windows.

Pour l'allumer, faîtes : "Menu démarrer", chercher l'invité de commandes (ou "cmd"), puis tapez "cd " suivie de l'adresse d'où se trouve le fichier "balabolka_txt.py" (voir dans la barre d'adresse de l'Explorateur de Fichiers). Puis tapez "cls&&python3 balabolka_txt.py", suivi de l'adresse de là où se trouvent les fichier à convertir.

Des options peuvent être ajoutées dans la commande (voir le fichier READ-ME.txt)

____

Utilisation plus détaillée, avec des exemples : 


Lorsque vous tapez des adresses, si elles contiennent des espaces, il faut ajouter des guillemets.

Par exemple :  cd "C:\Users\Nom Utilisateur\Dossier contenant les fichiers a convertir"

Sinon, ce n'est pas nécessaire (mais ça marche quand-même) :

Par exemple : cd C:\Users\Nom_Utilisateur\Dossier_contenant_les_fichiers_a_convertir


1) Ouvrir un terminal (ou invité de commandes)
2) Tapez cd <adresse où se trouve balabolka_txt.py>
3) Tapez la commande tu programme :


Exemples de commandes : 


python3 balabolka_txt.py -r "C:\Users\Nom_Utilisateur\Dossier_contenant_les_fichiers_a_convertir"

python3 balabolka_txt.py -v 2 "C:\Users\Nom_Utilisateur\Dossier_contenant_les_fichiers_a_convertir"

python3 balabolka_txt.py -v -r 2 "C:\Users\Nom_Utilisateur\Dossier_contenant_les_fichiers_a_convertir"

___

Le programme a été testé uniquement sous Windows 7 en 2019 et 2020.


Ne marche pas si le chemin ou les noms des fichiers contiennent des caractères non-ASCII.

(Enlever notamment les accents (é, à, etc...))

Si les fichiers à convertir en contiennent, ce n'est pas grave, en revanche. A condition que vous l'ayez enregistré en "ANSI".

Pour ce faire, prenez un texte, copiez-le dans un Notepad.exe (installé par défault sous tous les Windows), puis enregistrez le fichier en veillant à ce que le format indiqué à côté du nom du fichier dans la fenêtre d'enregistrement soit "ANSI". L'extension du fichier doit être ".txt"

___

A noter : 

J'ai remarqué que les fichiers qui contenaient plus de 300 000 charactères, environs, n'étaient pas convertis jusqu'au bout (bien que le programme ne s'interrompait pas et que la convertion durait très longtemps). C'est dû au programme Balabolka. J'ai commencé à créer des programmes (pour tenter de résoudre ce problème) :

1) Pour calculer le nombre de charactères d'un fichier
2) Pour séparer un fichier en plusieurs fichiers et les mettre dans un dossier temporaire créé pour l'occasion
3) Les convertir séparément
4) Refusionner les fichiers convertits en un seul fichier
5) Effacer les fichiers créés (sauf le fichier résultat) et le dossier temporaire créé pour l'occasion

J'en suis à l'étape 4. J'ai essayé d'utiliser FFMPEG, mais pas encore de résultats probants.
Pour le moment, je n'ai pas encore mis en ligne les programmes des étapes 1) à 3) (d'ailleurs le programme balabolka_txt était initialement simplement destiné à faire l'étape 3), mais finalement, j'ai pensé qu'il serait utile en lui-même et je l'ai modifié en conséquences).
