#rework #todo


-  version actuelle : **1.5.0**


- ## **objectifs**

	- gérer l'augmentation de complexité aux niveau des [[Item]] et de la différence de leur comportement suivant leurs différents modes :
		- in world
		- grabbed
		- placed

	- régler les problèmes d'optimisation lorsque des [[Usable]] sont **grabbed** en trop grande quantité pour rien ça fait de la soupe

	- remplacer le système de **prefabs** pour améliorer le workflow en unifiant les items dans des **ScriptableObjects** (ce que sont déjà les [[File]])

- ## **description du rework**

	- on splitte [[Item]] en plusieurs sous scripts qui intéragissent entre eux :
		- [[Item]] qui devient un **so**, garde la réference, son max stack, sa description etc tout ce qui est nécessaire à représenter l'item (donc aussi les **upgrades**)
			- !! - !! ça veut dire faut aussi stocker l'inventaire de l'Item ??????????

		- [[WorldItem]] est un container, est un monobehaviour [[Capable]] et reçoit donc des [[Capacity]]. Peut être poolé pour soulager le trash recuperer. contient aussi un rigidbody ainsi qu'une [[MoveCapacity]] dans le futur (pour le moment on a encore des [[Movable]] donc c movable mais bref).
			- --> si on drop un item de l'inventaire vers le sol ça le transforme en world item
		- [[PlacedItem]], pareil container, monobehaviour pas forcément capable mais a un [[AnimSystem]]. pas de rigidbody ni rien
			- --> si on met un item dans un InventoryPlacer ça créé un
			  placed item ? en plus que l'inventory gère son item de base
		- [[CapacityHolder]] ????
			- container qui stocke une **List<Usable**> et est le parent des [[Capacity]] des items prêtées au holder.
				- quand on grab un item qui contient des capacity spéciales, au lieu de détruire la capacity elle est confiée au capa holder puis l'item est stocké dans l'inventaire.
				- ensuite quand l'item est retiré de l'inventaire la capacity holder lui rend sa capacité, soit en l'ajoutant à un World item, soit en la transferant vers le nouveau capa holder. 
			- n'a pas d'affichage graphique mais qui garde en tête les usables qu'on a et gère leur physique directement (a les colliders de bouffe par exemple, ainsi que les trucs nécessaires pour que le [[Laptop]] reste en vie et fonctionne ?)
			- peut stocker une **List<Usable**>
			- --> si l'item qu'on vient de grab est un usable, ça le stocke normalement dns l'inventaire mais ajoute aussi l'usable au usable manager, qui met à jour ses colliders ainsi 


- ## **TODO**
	- [ ] 