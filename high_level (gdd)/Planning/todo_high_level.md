#planning

ce todo est différent du [[todo_low_level]] parce qu'il sert à détailler les prochaines étapes du [[ROADMAP]] d'un point de vue **Systèmes**. cela signifie que les reworks à l'intérieur des systèmes ne sont pas détaillés. on veut garder une vision d'ensemble.


# systems design & prototypage


- #### systemes ok tier
	- [[InventorySystem]]


- #### systemes en cours de rework/proto
	- [[RoomSystem]] && [[RoomSystem_Proto]]
	- [[CapableSystem]] && [[CapableSystem_Proto]]
	- [[CapacitySystem]] && [[CapacitySystem_Proto]]


- #### systèmes à rework
	- [[UI_Manager_Rework_2]]
	- [[Item]] & [[Item_Rework_1]]
	- [[Hacking]] & [[File]]
	- [[InputSystem]]


- #### systèmes encore inexistants (en cours de design)
	- [[SaveSystem]]
	- [[Ecosystem]]
		- **EnemyWaveSystem** meilleur nom ?
	- [[WallSystem]] / [[DoorSystem]] 
	- [[LevelSystem]] ? [[WorldSystem]] ?
	- [[Cinematics]]
	- [[AudioSystem]]



## hiérarchie des systèmes

- **World Tier**
	- [WorldSystem] - holds [WorldData]
	- [SaveSystem]
	- [EcoSystem]
	- [UI System] i guess ?
	- [Cinematics] ?????
- **Level Tier**
	- [LevelSystem] - holds [LevelData]
	- [WallSystem] ?
	- [DoorSystem] ???
- **Room Tier**
	- [RoomSystem] - holds [RoomData]
	- [MovableEngine]
- **Capable Tier**
	- [CapableSystem] - holds [CapableData]
	- [ControllerSystem]
	- [InventorySystem]
	- [AnimPlayer]
	- [AudioSystem] ?
- **Capacity Tier**
	- [MoveCapacity]
	- [Hacking]
	- [Combat]
	- etc en fait tous les systèmes plus petits de capacity en fait