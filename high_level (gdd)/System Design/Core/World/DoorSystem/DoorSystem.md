#system #designing

- [x] [[DoorSystem_Proto]]

---

# description

- **DoorSystem** est le système qui gère les différentes [[Door]]. C'est un sous système de [[RoomSystem]]. Il s'occupe d'appeler tilemap engine pour désactiver/activer les tilemaps [mask] de chaque [Room] lorsque c'est nécessaire.

- Pour cela le système stocke son propre graph de connexions de rooms/doors, [DoorGraph], qui est différent du [RoomGraph] car c'est un graph qui peut servir à la navigation aussi. pas visuel

---

# fonctionnement du système


## 0. DoorGraph

Ce sous système sert à stocker le graph de connexions de rooms/doors d'un level. Pour cela on stocke un système de [nodes/link]

- [node] représente un chunk/room
- [link] représente un passage potentiel entre deux [nodes]
	- il peut contenir une [door] ce qui modifie la navigation entre ces nodes

ce graph est construit automatiquement lorsque le world se load, on récupère toutes les doors puis on link les rooms séparées par une door
- > marche seulement si chaque [room] correspond à un [chunk].
- > lorsqu'on aura un autochunker, on pourra tracer des links entre tous les chunks d'une même room étant donné qu'on peut passer librement d'un chunk à l'autre au sein d'une même room


## 1. Ceiling Mask

pour utiliser la méthode visuelle il faut pouvoir cacher les rooms parfaitement. cela inclut :
- le ground
- les walls intérieurs
- les capables
- les particules
- les lights shadows

cela requiert l'utilisation du [MASQUE] et il correspond exactement au ceiling 'rempli' au lieu de son contour. cependant, l'opération de créer des rooms, la gestion du level etc des tilemaps ça devient lourd, long et peu agréable, on va donc plutôt chercher à [calculer algorithmiquement] les différentes tilemaps, et pour ça on a besoin d'un [WorldBuilder]

## 2. [[WorldBuilder]]

l'idée est simple : à partir du tracé du carpet + positions des doors sur ce carpet, on appuie sur un bouton et hop les tilemaps sont générées, avec même peut-etre différents chunks automatiquement découpés etc.

pour ça on doit pouvoir avec :
- un **node/link éditor** -> pour pouvoir placer les contours & doors d'une [Room] sur la [Grid]
- un **algorithme de mask** -> un pour chaque niveau, calcule successivement les différentes tilemaps, à savoir :
	- carpet
	- ground
	- walls intérieurs (caché lorsque la room est cachée)
	- walls exterieurs (visible meme lorsque la room est cachée)
		- > on peut peut etre garder les 2 ensembles si notre ceiling mask cache seulement les murs intérieurs, à tester
	- ceiling
	- ceiling mask



## 3. design meilleure methode

2 potentiels fonctionnements :

- soit purement [visuel] : le systeme **Show/Hide** les bonnes [[Room]] quand une Door est toggled.
	- [avantages] plus réaliste, simule les combats dans les pièces adjacentes
	- [inconvenients] rajoute du overhead au room system, demande une gestion des particules, lumières etc
		- [x] > peut se gérer d'un coup avec un [ceiling mask]
			- galère, pose d'autres soucis
		- > sinon on peut cacher les tilemaps et les capables directement
			- faisable si tous les capables ont le même shader de base

- soit purement [logique] : le système **Load/Unload** les [[Room]]
	- [avantages] moins d'overhead, reutilisation du [[RoomSystem]]
	- [inconvenients] peut-etre plus de travail sur le [[CapableSystem]] pour rendre réaliste les déplacements des movables au sein d'une room, peut-etre problème de lag aussi quand on ouvre une porte

votes :
- [visuel] : +4
	- [ceiling mask] : -1
	- [hide tilemaps + capables] : +1
- [logique] : -4

## .

---
# problèmes actuels

- [x] problème de [design] : faut tester quelle methode on veut choisir
	- > visuel à mille 1000%



---

# todo