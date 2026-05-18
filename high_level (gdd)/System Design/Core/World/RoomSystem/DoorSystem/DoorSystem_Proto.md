#rework #done 

-  version de création : **1.5.0r**
-  version de résolution : **1.5.0s**

---
- ## **objectifs**

	- créer une 1e versiond d'un room graph qui se calcule en awake et qui détermine les futurs rooms visibles en fonction de la room actuelle du controller & de l'état des doors du monde




---
- ## **TODO**


	- [x] lors du load d'une [Door] faut vérifier dans [[CapableSystem]] si au moins une des 2 rooms ne sont pas par hasard visible (pour le moment ça check que la room propriétaire je crois)

	
	- [x] les doors, comme n'importe quel capable, sont pop par le [[CapableSystem]] ?
	- [x] elles retiennent par contre dans leur [DoorData] 2 **room_ids** et elles trigger un event quand elles sont toggled
	- [x] [DoorEngine] récupère ces events, puis calcule quelles rooms doivent être cachées/affichées
	- [x] [DoorEngine] appelle les methodes Show() / Hide() de [TilemapEngine]