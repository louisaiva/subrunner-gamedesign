#rework #doing

-  version actuelle : **1.5.0c**

---

- ## **objectifs**
	- adapter les [[Capacity]] pour les intégrer dans le système actuel de pooling dynamique
	- mettre en place des [DataTemplates] qui nous permettent de dupliquer la data depuis une data stable plutôt que depuis une [Data] potentiellement changée




---

- ## **TODO**


	- [x] implémenter un [TemplateData] system qui permet de dupliquer les data des templates au lieu de les dupliquer depuis des capacités loaded
		- [x] renommer [capacities_datas] to [world_capacities_data]
		- [x] créer un dict [template_capacities_data]
		- [x] gérer le spawn de nouvelles capacities based on templates


	- [x] faire une [[HealthCapacity]] (au lieu de [[Being]])


	- [x] implémenter un virtual void SaveDynamicData() qui est appelé dans UnloadData() et qui fait rien mais toutes les capacités qui en découlent peuvent donc l'implémenter !


	- [ ] adapter [[SpawnCapacity]]
		- [x] stocker la data de l'entity id à load et les parametres de spawn
		- [ ] ajouter une [AnimLayerData] optionnelle à SpawnCapacityData


	- [ ] adapter [[WalkCapacity]] 
		- [ ] créer une [WalkData] qui sauvegarde :
			- [ ] par entité (donc save dynamiquement) [walk_percentage_target] + [walk_speed]
			- [ ] par template [max_speed]
		- 
		- [ ] regénère l'instance des footsteps au **Load()**
		- 
		- [ ] merge [RunCapacity] dans Walk
			- [ ] sauvegarde [run_speed] + [is_running]


	- [ ] adapter [[AttackCapacity]]
		- [ ] créer une [AttackData]
			- [ ] vitesse d'attaque
			- [ ] points dégats