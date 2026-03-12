#system #designing



# description

**LevelSystem** est le système qui gère les Levels. Il s'occupe de load/unload les Levels et donc demande à [[RoomSystem]] de charger les bonnes rooms.

# fonctionnement du système

Cycle de vie d'un [[Level]] (quand on appuie sur le bouton de l'ascenceur, le système se charge d'Attacher un Level, et ça fait les étapes suivantes) :
- charger la première [Room] voisine à l'ascenceur.
- charger les rooms suivantes en partant des plus proches en faisant des pauses de frames entre chaque loading



# problèmes actuels

- problème de **DESIGN** :
	- le level systeme devrait gérer les LEVELs mdr pas les rooms !
	- Est-ce que le RoomSysteme (qui gère les rooms) ne serait pas la réincarnation de [Level] et le LevelSysteme la réincarnation de [World] ?
		- -> pas vraiment parce que Level & World sont des [Object], pas des [System], mais y'a une idée de dimension équivalente, parce que Level gère une List de Room tout comme [RoomSystem] ?

- 



# reworks
- 