# LITReview

Site permettant de consulter ou de solliciter une critique de livres à la demande.

## Installation et Exécution

Si vous avez déjà installé Python, assurez-vous qu'il soit à jour.
Sinon, téléchargez et installez Python. [Site Web](https://www.python.org/downloads/)

Commencez par télécharger le repository en cliquant sur le menu "Code", puis "Download ZIP".

Extrayez le dossier. 

Dans celui-ci, créez et activez un environnement virtuel. Pour cela :
- Ouvrez votre terminal et placez-vous dans le dossier extrait,
- Exécutez la commande : `python -m venv env`,
- Exécutez ensuite la commande : `source env/bin/activate` (Sous Windows, l'activation se fera avec le fichier env/Scripts/activate.bat).

Toujours dans le terminal, installez les dépendances en exécutant la commande : `pip install -r requirements.txt`

Déplacez-vous dans le dossier "litreview_project" et exécutez la commande : `python manage.py runserver`

Dans votre navigateur, écrivez dans l'url : http://127.0.0.1:8000/

Vous pouvez vous connecter avec ce compte pour tester l'interface : yoan | test-test1