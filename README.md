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

## Compilation en .exe

Pour g\xe9n\xe9rer un ex\xe9cutable avec PyInstaller :

```bash
pyinstaller --onefile main.py
```

Les assets se trouvent dans le dossier `assets/` et pourront \xe9voluer
au fil du d\xe9veloppement.
