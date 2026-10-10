#planning 

-  version de création : **1.5.2d**
-  version de résolution : 

---
#### objectifs actuels :
- trouver du taf
- finaliser et peaufiner l'architecture de systèmes **Core** en réglant les différents problèmes, optimisations possibles présentes dans les dernières démos
- ajouter du [[Hacking]]
- diversifier le gameplay d'attaque & esquive
- avoir une première démo postable sur **Steam**

---


## CORE systems finalisation
- objectif : optimiser les systemes existants, corriger des erreurs de design en implémentant des solutions à prototyper (le design est globalement fini)

- **Capables** : séparer template/instance data avec 2 pipelines json et des attributs type [RuntimeOnly]
- **Chunks** : réécrire le loading/unloading des chunks en se basant sur les frontières de l'écran, ce qui va corriger beaucoup de bugs visuels et réduire drastiquement les frames drop
	- le réecrire sur le modèle de chargement des entités dans les chunks. cf [[ChunkLoader]]
	- mettre un gros collider idéalement [LineCollider2D] ? ou alors un énorme polygon collider qui épouse la forme du level afin de renforcer les murs pour pas que des items traversent


## Animation systeme rework

- vérifier certains bugs de performance check le postit Optimizations Possibles
- redessiner **Bob**, pour avoir des layers de jambes, de body et de hair, comme ça on peut parler en courant.
	- chaque layer possèderait donc sa propre liste de ACP ?
		- (AnimCapacityPriority)
		- cela demande un gros rework non ?

## Combat gameplay
- objectif : diversifier le gameplay de combat, jugé trop répétitif par les joueureuses

- diversifier les ennemis :
	- faire un ennemi à distance : petit drone qui lance des ptits missiles lents qui explosent
	- faire un ennemi in-dodgable : gros zombie lent qui fait d'autres attaques
	- faire un ennemi qui combine les deux : [usb]

- retravailler les animations :
	- raccourcir le rangement du katana dans l'attaque LR
	- dessiner des attaques en haut et en bas, voire même en diagonales
	- 

- faire que l'attaque et le dodge sont **time-based**. c'est à dire qu'elles peuvent être soit des attaques/dodge courts, soit des attaques/dodges chargées, si on maintient suffisament un treshold de time (qui est le même pour les deux touches)
	- l'attaque fait plus de dégat, ou alors on dessine ~~une nouvelle animation d'attaque ?~~
	- le dodge nous emmene plus loin
	- faire que le treshold soit suffisamment long pour que lorsqu'on fait un simple appui bah ça fasse tout le temps la même attaque qu'on a ajd

## Hacking
- objectif : réintégrer un premier système fonctionnel de hacking **ui-based**

- pas de hack through gameplay
- faire que les Files sont des Items, stockables sur un ordi serveur etc
- remettre le laptop
- on peut 


## lancement 1e démo steam
- deadline : 
- fixer la résolution à 16:9
- faire un shader pour la cinématique
- et faire un shader pour les traces de [Fred]