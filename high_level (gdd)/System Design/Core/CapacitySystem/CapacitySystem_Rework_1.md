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


	- [x] adapter [[WalkCapacity]] 
		- [x] créer une [WalkData] qui sauvegarde :
			- [x] par entité (donc save dynamiquement) [walk_percentage_target] + [walk_speed]
			- [x] par template [max_speed]
		- 
		- [x] regénère l'instance des footsteps au **Load()**
		- 
		- [x] merge [RunCapacity] dans Walk
			- [x] sauvegarde [run_speed] + [is_running]


	- [x] adapter [[AttackCapacity]]
		- [x] créer une [AttackData]
			- [x] vitesse d'attaque
			- [x] points dégats

	- [x] vérifier que l'AttackCapacity fonctionne vraiment bien
		- [x] des fois bugs avec le polygon collider du chat ?
			- jsaipa d'ou ça vient, debug ça
		- [x] bug de [excluded tags] dans l'[[AttackCapacity]], ce qui fait que les chats peuvent se faire des dégats entre eux (et zombies entre eux)
			- > certainement problème du tag de la [HealthCapacity] qui n'est pas la même que celui du [[Capable]] (+1)
			

	- [ ] comment faire pour que le chat retienne qu'on l'a attaqué ?
		- [ ] > utiliser la [SocialData]
		- [ ] > mid terme (+1) -> dépend de [[BrainSystem]]