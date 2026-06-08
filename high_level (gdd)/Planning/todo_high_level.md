#planning

ce todo est différent du [[todo_low_level]] parce qu'il sert à détailler les prochaines étapes du [[ROADMAP]] d'un point de vue **Systèmes**. cela signifie que les reworks à l'intérieur des systèmes ne sont pas détaillés. on veut garder une vision d'ensemble.


# systems design & prototypage


- #### systemes ok tier
	- [[InventorySystem]]
	- [[CapableSystem]]
	- [[CapacitySystem]]
	- [[ChunkSystem]]


- #### systemes en cours de rework/proto
	- [[WorldBuilder]]
	- [[DoorSystem]]
	- [[LevelSystem]]
	- [[WorldSystem]] 
	- [[SaveSystem]]


- #### systèmes à rework
	- [[MotorSystem]]
	- [[UI_Manager_Rework_2]]
	- [[Item]] & [[Item_Rework_1]]
	- [[Hacking]] & [[File]]
	- [[InputSystem]]
	- Capacities :
		- [[AnimSystem]]
		- [[BrainSystem]]


- #### systèmes encore inexistants (en cours de design)
	- [[EcoSystem]]
		- **EnemyWaveSystem** meilleur nom ?
	- [[WallSystem]]
	- [[ExpSystem]]
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


- **Room Tier**
	- [RoomSystem] - holds [RoomData]
	- [DoorSystem]
	- [TilemapSystem]
	- [LightSystem]
	- ~~[WallSystem] ?~~ no need for it

- **Chunk Tier**
	- [ChunkSystem] - holds [ChunkData]
	- [MovableEngine]

- **Capable Tier**
	- [CapableSystem] - holds [CapableData]
	- [ControllerSystem]
	- [InventorySystem]
	- [AnimPlayer]
	- [AudioSystem] ?

- **Capacity Tier**
	- [ExpCapacity]
	- [MotorCapacity]
	- [MoveCapacity]
	- [Hacking]
	- [Combat]
	- etc en fait tous les systèmes plus petits de capacity en fait