#rework #done

-  version actuelle : **1.5.0**

---
- ## **objectifs**
	- implémenter une premiere [MotorCapacity] qui sera affectée aux entités loadées **UNIQUEMENT**
	- implémenter une [MotorData] qui memorisera toutes les données nécessaires à cette fin
	- faire que cette capacity pool correctement les composants [GoapActionProvider] && [AgentBehaviour] du **GOAP system**




---
- ## **TODO**
	- [x] implémenter [MotorCapacity] & [MotorData]
	- [x] faire que ça se charge correctement avec le [[CapacitySystem]]
	- [x] pooler correctement action provider
	- [x] & Agent Behvaiour

	- [x] Tester avec 2 types d'actions / goal afin de vérifier que c'est réellement bien poolé
		- [x] faire un spawner à zombie + spawner à dev
		- [x] les dev doivent réparer des ordis jsp