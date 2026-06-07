#rework #done 

-  version actuelle : **1.5.0**

---
- ## **objectifs**
	- prototyper un BSOD pattern comme pour [[ChunkSystem]]
	- load/unload/spawn des capables dynamiquement
	- pouvoir assigner en direct des capacities à ces capables -> [[CapacitySystem]]
	- définir ce qui doit relever des capacités et ce qui doit relever du capable system
		- animplayer [<- capable]
		- body [<- capable]
		- inventory ? [<- capable]
		- brain ? capacité ? parce qu'on a besoin d'un [BrainSystem]
		- movable [<- capacité]
		- being [<- capacité]




---
- ## **TODO**



	- [x] update [CapableSystem] pour pouvoir switch un Capable into a [[Corpse]]


	- [x] ecrire **[[Item]].LoadData(CapableData data)** pour remettre à jour la data des items type reference, description, color etc etc


	- [x] [CapableBank] doit pouvoir pool des composants d'[AnimPlayer]
		- [x] [CapableData] doit donc avoir de la data pour les layers, leur position et leur skin
		- [x] ainsi que la animcapacitypriority list
		- [x] chaque layer (et meme AnimPlayer ?) doivent aussi stocker :
			- [x] le sr material
			- [x] le SortingLayer
			- [x] le sorting order

	- [x] si jamais on a des problèmes d'animations ça peut etre dû à l'assignation des [AnimCapacityPrio] list dans [[AnimSystem]] qui se fait dans l'Awake et donc pas dynamiquement dans le load player data...
	
	- [x] [CapableData] doit aussi gérer le
		- [x] Layer
		- [x] Tag

	- [x] [CapableBank] doit aussi pool les différents colliders utilisés de part et d'autres, que ce soit par les Capacity ou par les Capables en eux mêmes. Pour ça [Bank] a deux pools de colliders : box & circle
		- [x] remplacer **body** par **carpet** pour les objects ?
			- -> c que du naming donc pas nécessaire pour l'instant
		- [x] on peut avoir deux **body_prefab** différents dans [CapableBank], un pour les objects (donc direct layer objects + navigation modifier) et un pour les beings