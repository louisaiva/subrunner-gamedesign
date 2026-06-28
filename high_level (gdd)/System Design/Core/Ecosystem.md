#system #designing

- [ ] [[EcoSystem_Proto]]

---
# description

le but de ce système est de simuler un **EQUILIBRE** d'éco système ainsi que de gérer la **DIFFICULTE** du jeu.


---
# fonctionnement du système

C'est un système de type **EDO** qui comporte 3 composants :
- Une [Engine] : singleton [[EcoEngine]]
- De la [Data] : [NestData]
- Des [Objects] : [[NestCapacity]]

## [deprecated] Old Design

[[EcoEngine]] est appelée toutes les x frames, et à chaque fois qu'il est appelé il :

- loop à travers [[Level]]
	- calcule la **difficulté** actuelle
	- si manque de difficulté par rapport à la **target difficulté**, alors calcule combien/quel type d'entité on doit spawn.
	- on retient ce nombre+type d'entité pour chaque level, c'est ce qu'on appelle le compteur.

- ensuite on loop à travers tous les [[NestCapacity]] :
	- on regarde quel level c et si on **doit** lui donner une entité pour rééquilibrer (via notre compteur définit avant)
		- si non, on continue
		- si oui, on regarde si on **peut** lui donner une entité, via le **store_mode**
			- si oui, on lui donne et on update le compteur
			- si non on continue
	- ensuite on regarde si on doit spawner des entités en fonction des entités actuellement stored dans le spawner

## .

---
# problèmes actuels



---

# todo

- [x] adapter [[NestCapacity]]
	- [x] stocker la data de l'entity id à load et les parametres de spawn
	- [x] ajouter une [AnimLayerData] optionnelle à SpawnCapacityData