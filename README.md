# Projet narratif "Aventure de Max"

Ce dépôt contient les débuts d'un petit jeu 2D humoristique 
conçu avec Pygame. Le joueur incarne Max, un jeune homme autiste et
curieux qui découvre un monde semi-réel peuplé de ses amis.

## Lancer le jeu

Installez d'abord les dépendances :

```bash
pip install -r requirements.txt
```

Puis exécutez le fichier `main.py` :

```bash
python main.py
```

Les touches fléchées permettent de se déplacer et la barre
espace sert à parler aux personnages.
Au lancement, un écran titre propose "Nouvelle partie" ou "Quitter" ;
utilisez Haut/Bas et Entrée pour choisir.
Les noms des PNJ apparaissent au-dessus de leur tête.
Si Max atteint le bord bas de l'écran, une nouvelle zone se charge
(par exemple le bar de Nao).
Chaque zone possède ses propres PNJ et dialogues.
Un petit inventaire apparait en haut à gauche et peut contenir jusqu'à quatre objets remis par les personnages.

### Personnages disponibles

- **Léo** : premier ami rencontré.
- **Mathias** : prétend avoir arrêté la clope mais fume encore.
- **Denis** : passionné de gore et de provocations.
- **Nao** : barman parisien fêteur.
Chaque PNJ peut remettre un objet unique à Max après son dialogue
(`Stilnox 10mg`, `Briquet vide`, `Glock 17` ou `Canette 8.6 vide`).

## Compilation en .exe

Pour générer un exécutable avec PyInstaller :

```bash
pyinstaller --onefile main.py
```

Les assets se trouvent dans le dossier `assets/` et pourront évoluer
au fil du développement.
