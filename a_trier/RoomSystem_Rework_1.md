#rework #done

-  version actuelle : **1.5.0**

---
- ## **objectifs**
	- régler les problèmes de [logique] du RoomSystem
	- renommer en [RoomEngine]
	- forcer le fait qu'un seul [Capable] est relié à une seule [Room] à la fois
	- pouvoir handle des transitions entre différents neighbours
		- (> 2 neighbours)



	- #### /!\ [ATTENTION] /!\
	- le calcul de transition entre les rooms doit aussi pouvoir s'effectuer seulement via la position du movable + points de collider de la room
		- > version unloadée sans colliders !!
		- > sinon pour ça on s'en fiche que ça soit parfait on fait juste distance des centres ?

---
- ## **TODO**

	- [x] créer des hashset de vérité absolue dans [RoomEngine]
		- [x] roomByMovable : movable_id -> room_id
		- [x] movablesByRoom : room_id -> List<movable_id>
		- [x] dirtyMovables : List<movable_id>
			- > ces movables viennent de changer de room (ou n'ont pas encore de room assignées) et doivent donc être réassignés
	
	- [x] on doit pouvoir charger directement les bons capables2room dict dans le Start() de [RoomEngine] pcq pour le moment on le fait pas