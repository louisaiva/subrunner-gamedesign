#rework #done 

-  version actuelle : **1.5.0**

---
- ## **objectifs**
	- implémenter une premiere version du LevelSystem
	- pouvoir charger un [Level] à la fois (current level)
		- > pas besoin de LevelPooler
	- créer une première version d'un **Editor Tool** [RoomGraph] permettant de facilement créer le graph de voisinage




---
- ## **TODO**

	- [x] room graph
		- [x] avoir un design solide
		- [x] implémenter [RoomNode] qui marche seulement dans l'editor ?
			- [x] s'execute seulement en editor mode, affiche un cercle au milieu de la room qui peut etre cliqué dessus
		- [x] implémenter [RoomLink]
			- [x] faire qu'un click sur la node lance la création d'un link
			- [x] si on clique sur un deuxieme node alors le link est créé
			- [x] assigne les voisins aux 2 rooms et