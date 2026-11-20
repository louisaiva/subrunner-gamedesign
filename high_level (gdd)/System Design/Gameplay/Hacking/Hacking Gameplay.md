#system #designing

- [x] [[Hacking_Proto]]
- [ ] [[Hacking_Rework_1]]


---
# description

Le systeme de **Hacking** est un élément central du jeu, et surtout du gameplay. C'est ça qui offre tout le côté intéressant de l'exploration. CAD des récompenses, des défis, du challenge, et des énigmes.

Il est composé en deux parties différentes, basée sur le même système backend de hacking :

- le HACKING STATIQUE :
	- aussi appelé **ui-based hacking**
	- hack fait en appuyant sur des [[UI_Slot]] dans les menus de device, notamment [[UI_Laptop]], [[UI_Computer]], etc

- le HACKING DYNAMIQUE :
	- **in-game hacking**
	- hack rapide de "combat", type sorts de magie avec mana des sorciers dans les rpg
	- se lance en combinant [JOY-R] & [RT]


---
# fonctionnement du système


## 1. ui-based hacking

## 2. in-game hacking

Controls :

- gamepad :
	- [JOY-R] --> fait selectionner la hack-target
	- puis [RT] --> lance le hack

	- [RT] --> ouvre la pool de selection d'exploit [[UI_ExploitWheelPool]]
	- puis [JOY-R] --> selectionne l'exploit

- mouse :
	- [RMB] --> hold + move --> selectionne la hack-target, lance le hack on mouse button release
	- [CMB] (molette) --> hold + move --> ouvre la pool de selection, selectionne l'exploit en bougeant et valide en relachant le bouton molette
	- [CMB] (molette) --> scroll --> scroll dans les exploits sans afficher la pool 



---
# problèmes actuels

- problème de [design] : 
	- déplacement de files dans un autre disk doit les copier ????? semble compliqué à faire ?
	- sinon on peut déplacer les fichiers, mais on risque de perdre un ou plusieurs files à terme ??? remarque on peut pas drop les files donc c'est pas si mal
		- j'aime bien cette idée. au pire on met un ordinateur central au **QG** qui permet de récupérer des fichiers supprimés. stocke tous les fichiers qu'on a trouvés de la partie. affiche le nombre de fichiers existants aussi d'ailleurs.


---
# todo
- [ ] 