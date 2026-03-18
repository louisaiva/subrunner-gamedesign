#rework #doing

-  version actuelle : **1.5.0c**

---
- ## **objectifs**
	- adapter les [[Capacity]] pour les intégrer dans le système actuel de pooling dynamique
	- mettre en place des [DataTemplates] qui nous permettent de dupliquer la data depuis une data stable plutôt que depuis une [Data] potentiellement changée




---
- ## **TODO**


	- [ ] implémenter un [TemplateData] system qui permet de dupliquer les data des templates au lieu de les dupliquer depuis des capacités loaded
		- [ ] renommer [capacities_datas] to [world_capacities_data]
		- [ ] créer un dict [template_capacities_data]
		- [ ] gérer le spawn de nouvelles capacities based on templates


	- [ ] faire une [[HealthCapacity]] (au lieu de [[Being]])





	- [ ] adapter [[Brain]] en un [[BrainSystem]]

	- [ ] adapter [[SpawnCapacity]]
		- [x] stocker la data de l'entity id à load et les parametres de spawn
		- [ ] ajouter une [AnimLayerData] optionnelle à SpawnCapacityData


	- [ ] faire une [[MoveCapacity]] (au lieu d'un [[Movable]])
		- [x] comment on gère le rigidbody ???
			- on le laisse sur le capable blc !! une fois qu'il est ajouté par [[CapableBank]] bah après c parf il se désactive tout seul lorsqu'on décharge le capable, donc c parf
				- ah ouais ? du coup ça veut dire il sera quand même sur les items même dans un inventaire ?
					- oui mais tfacons idéalement on pourrait ne pas charger les items dans l'inventaire mdr