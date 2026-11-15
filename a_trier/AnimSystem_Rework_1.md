#rework #todo

-  version de création : **1.5.2f**
-  version de résolution : 

---
- ## **objectifs**
	- 




---
- ## **TODO**

	- vérifier certains bugs de performance check le postit **Optimizations Possibles**
	- redessiner **Bob**, pour avoir des layers de jambes, de body et de hair, comme ça on peut parler en courant.
		- chaque layer possèderait donc sa propre liste de ACP ?
			- (AnimCapacityPriority)
			- cela demande un gros rework non ?
	- réflechir aux problèmes de l'utilisation de plusieurs layers et des différentes directions
		- les layers compliquent la tache de dessin : ou alors faut faire plein de layers différents, ex : on dessine **USB**; idéalement en LR il a un bras devant, puis la tete, puis le corps, puis le dernier bras. **MAIS** en D il a la tete puis les deux bras pui le corps, **ET ENFIN** en U il a la tete puis le corps puis
			- faudrait que chaque **animation de capacity** puisse modifier l'index des **layers** de l'anim player en temps réel.
			- et en relier des nouvelles ?
			- faudrait que ça soit stocké dans **Anim** en fait
				- d'ailleurs **Anim** c'est quoi ? faudrait pas tout rebossé ça en **AnimData** ??
	- bref ça demand"e un gros rework core là
