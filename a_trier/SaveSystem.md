#system #designing

- [ ] [[prototype]]


---
# description

[SaveSystem] est un système un peu éparse qui relie toutes les différentes [Data] des systèmes [[DEBO]] afin de pouvoir sauvegarder l'état du monde à un instant T

On peut ensuite charger cette "save" ce qui équivaut à charger un "world" en réalité


---
# fonctionnement du système


## 1. WorldSave / LevelSave life cycle

Une [WorldSave] est en réalité principalement constituée de plusieurs [LevelSave] qui, ensembles, définissent l'état du world.

le cycle de vie d'une [WorldSave] est donc relativement simple :

![[image-1.png]]

le cycle de vie d'une [LevelSave], est, quant à lui, plus tumultueux :

![[image-2.png]]

comme on peut le voir il y a donc 2 types de [LevelSaver] différents :


## 2. Static Save

- soit depuis l'inspecteur dans l'Editor (save manuelle)
- soit potentiellement depuis un [WorldBuilder] ?

- sauvegarde :
	- les doors
	- les rooms :
		- les tilemaps
		- les lights

- cela signifie qu'on doit aussi :
	- redessiner le room graph neighbourhood, ce qui est relou (ou doit se faire automatiquement)
	- rebuild les navmesh
	- regrab tous les capables, y compris les doors

> cette save doit donc se faire depuis un [Level] constitué en un seul gameobject regroupant :
> 	- les rooms
> 	- les tilemaps
> 	- les doors
> 	- les lights
> 	- les capables (objects + movables)

## 3. Dynamic Save

- sauvegarde :
	- la position des movables
	- la PlayerData
	- la dynamique data des doors (fermé/ouvert)

- les tilemaps, les rooms, les lights sont statiques donc pas besoin de sauvegarder ça !
	- en plus pas besoin de regrab les capables pcq on connait quelle room possède quoi

> on peut donc potentiellement faire cette save en full runtime pendant qu'on joue -> associer un bouton save dans les options [[UI_PauseMenu]]


## .

---
# problèmes actuels

- problème de [workflow] :
	- on doit donc pouvoir rewrite par dessus un [level-all-in-one] pour re assigner les doors, capables etc
	- on doit donc pouvoir charger un [level-all-in-one] at runtime ?




---
# todo

- [x] sauvegarder la [version] du jeu dans [WorldData]
- [ ] continuer le design