#system #designing

---
# description

**AudioSystem** est le système qui gère tout l'audio du jeu lol
Il sert de pont entre **FMOD** et le jeu afin d'offrir certaines methodes simples à appeler de n'importe où pour jouer du son




---
# fonctionnement du système

Ce système est composé de 2 composants principaux, tous deux **singleton**:

- ## 1. AudioEngine
	- l'engine qui sert de porte d'entrée au système.
	- Propose la méthode principale **PlaySound()** qui prend soit directement une [EventReference] de fmod, soit un **skin** + **capacity** et qui va faire les bons calls à la [Bank] pour récupérer le bon [EventReference], puis le jouer.

- ## 2. AudioBank
	- la [Bank] qui stocke toutes les [EventReference]
	- peut être appelée par n'importe quel script mais en vrai surtout par [Engine] comme ça ça simplifie pas mal de choses

la plupart des calls à **AudioEngine.Instance.PlaySound()** doivent se faire directement depuis les [[AnimSystem]] pour faciliter l'intégration du son avec les visuels



---
# problèmes actuels

- problème de [workflow] : 
	- est-ce qu'on peut mettre directement des layers de son dans **FMOD** ? flemme de devoir passer par [Studio One] seulement pour exporter les sons puis les réinsérer dans [FMOD] puis enfin les récup dans [Unity]... surtout si c'est pour se rendre compte que ça marche pas et qu'on doit re manipuler dans so...


---
# reworks
- 