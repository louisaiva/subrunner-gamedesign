#planning 

-  version de création : **1.5.2d**
-  version de résolution : 

---
#### objectifs actuels :
- **trouver du taf**
- finaliser et peaufiner l'architecture de systèmes **Core** en réglant les différents problèmes, optimisations possibles présentes dans les dernières démos, et **revoir le système global d'animation 2D**
- diversifier le [[gameplay d'attaque & esquive]]
- ajouter du [[Hacking]]
- avoir une première démo postable sur **Steam**

---


## CORE systems finalisation
- objectif : optimiser les systemes existants, corriger des erreurs de design en implémentant des solutions à prototyper (le design est globalement fini)

- **Capables** : séparer template/instance data avec 2 pipelines json et des attributs type [RuntimeOnly]
- **Chunks** : réécrire le loading/unloading des chunks en se basant sur les frontières de l'écran, ce qui va corriger beaucoup de bugs visuels et réduire drastiquement les frames drop
	- le réecrire sur le modèle de chargement des entités dans les chunks. cf [[ChunkLoader]]
	- mettre un gros collider idéalement [LineCollider2D] ? ou alors un énorme polygon collider qui épouse la forme du level afin de renforcer les murs pour pas que des items traversent


## Animation systeme rework

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


## Combat gameplay : [[gameplay d'attaque & esquive]]


## Hacking
- objectif : réintégrer un premier système fonctionnel de hacking **ui-based**

- pas de hack through gameplay
- **faire que les Files sont des Items**, stockables sur un ordi serveur etc
- remettre le laptop
- on peut 


## lancement 1e démo steam
- deadline : 
- fixer la résolution à 16:9
- faire un shader pour la cinématique
- et faire un shader pour les traces de [Fred]