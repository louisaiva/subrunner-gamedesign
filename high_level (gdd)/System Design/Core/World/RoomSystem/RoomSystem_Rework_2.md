#rework #todo

-  version actuelle : **1.5.0**

---
- ## **objectifs**
	- faire que les entités qui sortent de la [Zone chargée] soient basculées dans leur nouvelle [Room] et donc se font décharger dynamiquement




---
- ## **TODO**

	- [x] des fois quand on unload une room ça unload ses entités, et donc ça trigger [OnRoomExit], ce qui recalcule une nouvelle room qui est parfois faussée pour des entités...
		- > ça casse tout parce que si la nouvelle room associée est déjà loadée, bah les entités viennent de se faire unload donc la room est loadée mais pas les entités
		- > quand on reload l'ancienne room, ça load pas du tout les entités du coup elles disparaissent pouf

	- [x] gérer le spawn/despawn des capables & des items mieux
	- [x] faire que ça appelle une seule fois la recalculation de la best room ça serait mieux

	- [x] faire que [RoomEngine] soit "event based" plus que "trigger based" pcq sinon on va avoir des problèmes pour les entités qui sont unloadées et qui font des trucs (spawn, despawn, grab drop des items, etc)