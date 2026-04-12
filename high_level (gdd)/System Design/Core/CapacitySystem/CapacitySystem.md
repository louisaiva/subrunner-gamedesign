#system #designing

- [x] [[CapacitySystem_Proto]]
- [ ] [[CapacitySystem_Rework_1]]


---
# description

**CapacitySystem** est le système de base qui gère les capacités, notamment leur chargement/déchargement et pooling dans [CapacityBank]

Audit des capacities nécessaires/inutiles et dont la data doit être saved/pas saved : [[Capacity Utility And Save Policy Audit]]



---
# fonctionnement du système









---
# problèmes actuels




---
# todo

- [ ] [long-term] faire une [[MoveCapacity]] (au lieu d'un [[Movable]])
	- [x] comment on gère le rigidbody ???
		- on le laisse sur le capable blc !! une fois qu'il est ajouté par [[CapableBank]] bah après c parf il se désactive tout seul lorsqu'on décharge le capable, donc c parf
			- ah ouais ? du coup ça veut dire il sera quand même sur les items même dans un inventaire ?
				- oui mais tfacons idéalement on pourrait ne pas charger les items dans l'inventaire mdr