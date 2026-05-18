#planning

ce todo est différent du [[todo_low_level]] parce qu'il sert à détailler les prochaines étapes du [[ROADMAP]] d'un point de vue **Systèmes**. cela signifie que les reworks à l'intérieur des systèmes ne sont pas détaillés. on veut garder une vision d'ensemble.


# systems design & prototypage


- #### systemes ok tier
	- [[InventorySystem]]
	- [[CapableSystem]]
	- [[CapacitySystem]]
	- [[RoomSystem]]


- #### systemes en cours de rework/proto
	- [[WorldBuilder]]
	- [[MotorSystem]]
	- [[LevelSystem]]
		- [[DoorSystem]]
	- [[WorldSystem]] 


- #### systèmes à rework
	- [[UI_Manager_Rework_2]]
	- [[Item]] & [[Item_Rework_1]]
	- [[Hacking]] & [[File]]
	- [[InputSystem]]
	- Capacities :
		- [[AnimSystem]]
		- [[BrainSystem]]


- #### systèmes encore inexistants (en cours de design)
	- [[Ecosystem]]
		- **EnemyWaveSystem** meilleur nom ?
	- [[WallSystem]] / 
	- [[SaveSystem]]
	- [[Cinematics]]
	- [[AudioSystem]]
	- [TV_System] ? ou alors c une [[UI_Pool]] ?



## hiérarchie des systèmes

- **World Tier**
	- [WorldSystem] - holds [WorldData]
	- [SaveSystem]
	- [EcoSystem]
	- [UI System] i guess ?
	- [Cinematics] ?????

- **Level Tier**
	- [LevelSystem] - holds [LevelData]
		- [DoorSystem]

	- [WallSystem] ?

- **Room Tier**
	- [RoomSystem] - holds [RoomData]
	- [MovableEngine]

- insérer un **Chunk Tier** ?
	- > permettrait de faire la distinction entre une room & un chunk, ce qui permet de découper des rooms en plusieurs petites

- **Capable Tier**
	- [CapableSystem] - holds [CapableData]
	- [ControllerSystem]
	- [InventorySystem]
	- [AnimPlayer]
	- [AudioSystem] ?

- **Capacity Tier**
	- [MotorCapacity]
	- [MoveCapacity]
	- [Hacking]
	- [Combat]
	- etc en fait tous les systèmes plus petits de capacity en fait