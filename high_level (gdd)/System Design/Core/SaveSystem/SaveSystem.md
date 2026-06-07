#system #designing

- [ ] [[SaveSystem_Proto]]


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


## 2. Static Save (AIO Save)

- soit depuis l'inspecteur dans l'Editor (save manuelle)
- soit directement depuis le [[WorldBuilder]] après un Build de Level
- sauvegarde des [AIO_Level] (all in one level)

- sauvegarde :
	- les doors
	- les rooms :
		- les tilemaps
		- les lights

- cela signifie qu'on doit aussi :
	- [x] redessiner le room graph neighbourhood, ce qui est relou (ou doit se faire automatiquement)
	- rebuild les navmesh
	- [x] regrab tous les capables, y compris les doors
	- [x] regénérer ids

> cette save doit donc se faire depuis un [AIO_Level] constitué en un seul gameobject regroupant :
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




## 4. SubSystems

Pour aider le [SaveSystem] on a besoin de différents subsystems, notamment :

- [AIO_Loader]
	- utilisé principalement par le [LevelTranslator] pour load un level spécifique en mode AIO pour ensuite override ses rooms/capables pour ensuite re save le level
	- aussi utilisé à chaque load de [[Level]] afin de bake le navmesh via le [[LevelNavBaker]]

## .

---
# problèmes actuels

- problème de [workflow] :
	- on doit donc pouvoir rewrite par dessus un [level-all-in-one] pour re assigner les doors, capables etc
	- on doit donc pouvoir charger un [level-all-in-one] at runtime ?
		- > oui (+3) -> [AIO_Loader] subsystem




---
# todo

- [x] sauvegarder la [version] du jeu dans [WorldData]
- [ ] continuer le design