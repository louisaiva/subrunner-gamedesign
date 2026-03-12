#rework #todo

-  version actuelle : **1.5.0**



---
- ## **objectifs**
	- [x] implémenter la base du système de pooling
	- [x] tester avec une [[HoverCapacity]]





---
- ## **TODO**
	
	- [x] maintenant on veut pouvoir drop des **Items** et les récuperer correctement, pour ça on doit
		- [x] unload la [[HoverCapacity]] at runtime quand on grab, 
		- [x] mais certaines capacités doivent rester actives même dans l'inventaire


	- [ ] faire une [[MoveCapacity]] (au lieu d'un [[Movable]])
		- [x] comment on gère le rigidbody ???
			- on le laisse sur le capable blc !! une fois qu'il est ajouté par [[CapableBank]] bah après c parf il se désactive tout seul lorsqu'on décharge le capable, donc c parf
				- ah ouais ? du coup ça veut dire il sera quand même sur les items même dans un inventaire ?
					- oui mais tfacons idéalement on pourrait ne pas charger les items dans l'inventaire mdr
	
	- [ ] une [[HealthCapacity]] (au lieu de [[Being]])
	
	- [ ] faire une interface pour les capacities necessitant un *cooldown*

	- [ ] adapter [[Brain]] en un [[BrainSystem]]