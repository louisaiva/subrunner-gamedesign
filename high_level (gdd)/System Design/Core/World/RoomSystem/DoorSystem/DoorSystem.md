#system #designing

- [x] [[DoorSystem_Proto]]
- [ ] [[DoorSystem_Rework_1]]

---

# description

- **DoorSystem** est le système qui gère les différentes [[Door]]. C'est un sous système de [[ChunkSystem]]. Il s'occupe d'appeler tilemap engine pour désactiver/activer les tilemaps [mask] de chaque [Room] lorsque c'est nécessaire.

- Pour cela le système stocke son propre graph de connexions de rooms/doors, [DoorGraph], qui est différent du [RoomGraph] car c'est un graph qui peut servir à la navigation aussi. pas visuel

---

# fonctionnement du système


## 0. DoorGraph

Ce graph gère les connexions de rooms/doors d'un level. Pour cela on stocke un système de [nodes/link]

- [node] représente un chunk/room
- [link] représente un passage potentiel entre deux [nodes]
	- il peut contenir une [door] ce qui modifie la navigation entre ces nodes

ce graph est construit automatiquement lorsque le world se load, on récupère toutes les doors puis on link les rooms séparées par une door
- > marche seulement si chaque [room] correspond à un [chunk].
- > lorsqu'on aura un autochunker, on pourra tracer des links entre tous les chunks d'une même room étant donné qu'on peut passer librement d'un chunk à l'autre au sein d'une même room
	- > même mieux maintenant qu'on a 2 niveaux, chunks & room on s'en tape des chunks en fait





## .

---
# problèmes actuels

- [ ] est-ce vraiment utile que [DoorData] stocke 2 [chunk_id] plutot que 2 [room_id] ??????
	- > non je pense vaut mieux tej tout et rester avec des [room_id] plutot que des [chunk_id]
		- > oui ==+1==


---

# todo