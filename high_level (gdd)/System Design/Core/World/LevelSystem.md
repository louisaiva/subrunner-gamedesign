#system #designing

- [x] [[LevelSystem_Proto]]
- [ ] [[LevelSystem_Rework_1]]


---
# description

**LevelSystem** est le système qui gère les Levels. Il s'occupe de load/unload les Levels et donc demande à [[RoomSystem]] de charger les bonnes rooms.



---
# fonctionnement du système

3 scripts sont utiles :
- [LevelEngine] :
	- load / unload le current level
	- (intègre le pooler pcq pas besoin de dynamic pooling vu qu'on a qu'un seul level à la fois & pas bcp de levels)
- [Level] :
	- stocke la data
	- appelle [[RoomSystem]] pour loader les rooms correspondantes
- [LevelData] :
	- données du [Level]. inclut aussi bien le navmesh data, que les rooms_ids et aussi la future data dynamique ?

[LevelEngine] est aussi utile pour différentes autres choses notamment :

### 1. [[RoomGraphDesign]]

### 2. Pathfinding

chaque [Level] gère aussi son pathfinding, en stockant les données du bon graph. Quand on bake le graph, ça bake le graph du level actuel seulement et l'enregistre dans [Level].

### 3. chargement d'un Level via [[Elevator]]

Cycle de vie d'un [[Level]] (quand on appuie sur le bouton de l'ascenceur, le système se charge d'Attacher un Level, et ça fait les étapes suivantes) :
- charger la première [Room] voisine à l'ascenceur.
- charger les rooms suivantes en partant des plus proches en faisant des pauses de frames entre chaque loading




### .

---
# problèmes actuels

- comment on gère les [Door] ? dans les link ? alors on doit avoir autre chose que juste les neighbours référencés dans la RoomData, on doit :
	- soit avoir des datas pour les doors
	- soit avoir un LinkRoomData qui gère les neighbours + doors + autres trucs




---
# todo


