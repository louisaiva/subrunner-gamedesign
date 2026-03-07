#rework #todo

-  version actuelle : **1.5.0**



---
- ## **objectifs**
	- implémenter la base du système de pooling
	- tester avec une [[HoverCapacity]]





---
- ## **TODO**
	
	- [ ] maintenant on veut pouvoir drop des **Items** et les récuperer correctement, pour ça on doit
		- [ ] unload la [[HoverCapacity]] at runtime quand on grab, 
		- [ ] mais certaines capacités doivent rester actives même dans l'inventaire
		- [ ] ainsi que tej le feet ça n'a aucun sens : faire une **[[MoveCapacity]]** au lieu d'un [[Movable]] !!!!


	- [ ] faire une [[MoveCapacity]] (au lieu d'un [[Movable]])
		- [ ] comment on gère le rigidbody ???
			- on le laisse sur le capable blc !! une fois qu'il est ajouté par [[CapableBank]] bah après c parf il se désactive tout seul lorsqu'on décharge le capable, donc c parf
				- ah ouais ? du coup ça veut dire il sera quand même sur les items même dans un inventaire ?
	
	- [ ] une [[HealthCapacity]] (au lieu de [[Being]])
	
	- [ ] faire une interface pour les capacities necessitant un *cooldown*
