# Projet narratif "Aventure de Max"

Cette r\xe9pository contient les d\xe9buts d'un petit jeu 2D humoristique 
con\xe7u avec Pygame. Le joueur incarne Max, un jeune homme autiste et
curieux qui d\xe9couvre un monde semi-r\xe9el peupl\xe9 de ses amis.

## Lancer le jeu

Installez d'abord les d\xe9pendances :

```bash
pip install -r requirements.txt
```

Puis ex\xe9cutez le fichier `main.py` :

```bash
python main.py
```

Les touches fl\xe9ch\xe9es permettent de se d\xe9placer et la barre
espace sert \xe0 parler aux personnages.
Au lancement, un \xe9cran titre propose "Nouvelle partie" ou "Quitter" ;
utilisez Haut/Bas et Entr\xe9e pour choisir.
Les noms des PNJ apparaissent au-dessus de leur tete.
Si Max atteint le bord bas de l\'\xe9cran, une nouvelle zone se charge
(par exemple le bar de Nao).
Chaque zone poss\xe8de ses propres PNJ et dialogues.
Un petit inventaire apparait en haut \xe0 gauche et peut contenir jusqu'\xe0 quatre objets remis par les personnages.

### Personnages disponibles

- **L\xe9o** : premier ami rencontr\xe9.
- **Mathias** : pr\xe9tend avoir arr\xeat\xe9 la clope mais fume encore.
- **Denis** : passionn\xe9 de gore et de provocations.
- **Nao** : barman parisien f\xeateur.
Chaque PNJ peut remettre un objet unique \xe0 Max apr\xe8s son dialogue
(`Stilnox 10mg`, `Briquet vide`, `Glock 17` ou `Canette 8.6 vide`).

## Compilation en .exe

Pour g\xe9n\xe9rer un ex\xe9cutable avec PyInstaller :

```bash
pyinstaller --onefile main.py
```

Les assets se trouvent dans le dossier `assets/` et pourront \xe9voluer
au fil du d\xe9veloppement.
