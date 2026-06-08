#system #designing

- [x] [[CapacitySystem_Proto]]
- [x] [[CapacitySystem_Rework_1]]
- [ ] [[CapacitySystem_Rework_2]]


---
# description

**CapacitySystem** est le système de base qui gère les capacités, notamment leur chargement/déchargement et pooling dans [CapacityBank]

**très similaire au [[CapableSystem]], légèrement moins rigide cependant**



Audit des capacities nécessaires/inutiles et dont la data doit être saved/pas saved : [[Capacity Utility And Save Policy Audit]] (ia)


---
# fonctionnement du système

les [Capacity] (objects) sont loadées instantannément et à la demande un peu via [CapacityEngine] (engine) qui envoie la (data) [CapacityData] à [CapacityBank] (bank/pooler) qui enfin instancie/etc/pool les objects et les renvoits.

Certaines capacity ont été simplifiées en des [SubSystèmes] :
- [[DropEngine]]

## - Engine
## - Data
## - Objects
## - Bank







---
# problèmes actuels


- [ ] comment faire pour que le chat retienne qu'on l'a attaqué ?
	- [ ] > utiliser la [SocialData]
	- [ ] > mid terme (+2) -> dépend de [[BrainSystem]]


---
# todo


- [ ] [[EatCapacity]] small rework
	- [ ] système de bouchées
	- [ ] dès que l'animation s'arrête, on arrête de manger
	- [ ] si on se prend un dégat pendant qu'on mange on drop notre bouffe
	- [ ] ajouter un mini ui - in game pour indiquer la quantité de bouchées restantes avec une barre


- [ ] [[DieCapacity]]

- [ ] [long-term] faire une [[MoveCapacity]] (au lieu d'un [[Movable]])
	- [x] comment on gère le [rigidbody] ???
		- on laisse le [rb] sur le capable blc !! une fois qu'il est ajouté par [[CapableBank]] bah après c parf il se désactive tout seul lorsqu'on décharge le capable, donc c parf
			- ah ouais ? du coup ça veut dire il sera quand même sur les items même dans un inventaire ?
				- oui mais tfacons idéalement on pourrait ne pas charger les items dans l'inventaire mdr (+1)
					- mdr le boss
				- ça change rien pcq [[Movable]] override les items avec l'effet **BeingGrabbed** 