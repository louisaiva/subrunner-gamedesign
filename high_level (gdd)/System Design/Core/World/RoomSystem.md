#system #designing

- [x] [[RoomSystem_Proto]]
- [x] [[RoomSystem_Rework_1]]
- [ ] [[RoomSystem_Rework_2]]

---
# description

**RoomSystem** est le système qui gère les rooms et donc les entités qui y sont situés actuellement
C'est un peu un système de chunk


---

# fonctionnement du système

### 1. Colliders

les [[Room]] ont une délimitation précise et hébergent les entités en temps réel. Ces [Room] storent les [[Capable]] qui sont dans cette délimitation.
- on fait comment pour définir la délimitation ? via chunk ? via collider2D ?
	- -> pour l'instant j'ai fait en [Polygon2D] pcq c plus simple à storer mais si on a des problèmes de perf tester avec [CompositeCollider2D] + box2D ou encore [EdgeCollider2D]

### 2. Zone chargée

Le script [[RoomSystem]] s'occupe d'activer seulement les bonnes Room, qui sont :
- la Room où le perso controllé est situé
- les Room adjactenes à cette Room principale

Ces rooms loadées forment ce qu'on appelle la "**Zone Chargée**"

Ces Room sont donc les seules à avoir des [Capable] dans des [GameObject] avec leurs Capacities chargées et tout
Toutes les autres Rooms (et donc la gestion de leurs entités) sont contrôlées en backend par [RoomSystem] pour garantir une optimisation opée

Le **RoomSystem** se charge donc de charger / décharger les différentes rooms en fonction de la position du perso, et donc il doit aussi appeler [[CapableSystem]].**LoadCapable / UnloadCapable** afin d'afficher seulement les bons mobs dans les bonnes rooms.

### 3. Update de la zone chargée

à chaque changement de room du Perso, on doit redefinir la zone chargée

dans l'update :
- on traque la position du perso
	- on vérifie qu'on a pas changé de room
	- **si on a changé de room** :
		- on met à jour les rooms voisines
		- on charge petit à petit les nouvelles et déchargent les anciennes ?
- 
- sinon on parcourt toutes les rooms :
	- **si elle est active (room principale + voisines):**
		- on update le movableengine pour les mobs de la room
		- 
	- **si elle est inactive (les autres)** :
		- on cycle à travers tous les mobs contenus dans la room
		- on update leur action virtuellement :
			- au lieu de faire des checks de collisions et des déplacements,
			- la room contient toute la data nécessaire à la réalisation d'une action (position de machin, inventaire de machin, skin de bidule)
			- on skip donc tous les déplacements qu'on retient virtuellement au sein d'une [GoalData]?
			- puis toutes les x frames on fait une update, et si on est arrivé au lieu de l'action, alors on l'effectue, mais pareil on a pas de capacité ni de collider, en fait on demande juste à [[LevelEngine]] ? la donnée dont on a besoin, on change un item d'inventaire
			- une action pareil, prend un certain temps virtuel à s'effectuer comme ça ça donne une impression réelle et ça désengorge le cpu


### .

---


# problèmes actuels


- [ ] est-ce qu'on a vraiment besoin de gérer les transitions de movables loadés to unloadés ? ça peut amener des bugs, trucs bizarres et demande pas mal de perf
	- [ ] sinon on peut juste gérer toutes les transitions de room des entités via [[MotorSystem]] et seulement gérer les transitions de room du perso via [[RoomSystem]]
		- > problème [MotorEngine] ne gère que les entités unloadées ?
		- > problème potentiel de realisme vu que c'est au feeling

- [x] des fois quand on unload une room ça unload ses entités, et donc ça trigger [OnRoomExit], ce qui recalcule une nouvelle room qui est parfois faussée pour des entités...
	- > ça casse tout parce que si la nouvelle room associée est déjà loadée, bah les entités viennent de se faire unload donc la room est loadée mais pas les entités
	- > quand on reload l'ancienne room, ça load pas du tout les entités du coup elles disparaissent pouf