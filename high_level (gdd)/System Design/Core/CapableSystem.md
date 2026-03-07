#system #designing


# description

le **capable system** est le système qui se charge de gérer toutes les entités et les capabilités.

C'est un système de type [[BSOD Pattern Design]] qui comporte 4 composants :
- Bank : [CapableBank]
- System : [CapableSystem]
- Object : les [[Capable]]. ce sont les gameobjects réels, instanciés et poolés par [[CapableBank]]
- Data : [[CapableData]]. gérés par le [System] et associés à des [Object] pour donner l'individu final loadé
	- data possède une [CapableID] c'est ça qui définit l'individualité du capable en fait


---

# fonctionnement du système

- ## 1. [CapableSystem]
	- le but de ce script est de gérer les capable en batch afin d'améliorer certaines perfs. Il doit permettre :
		- [x] d'etre la porte d'entrée de ce systeme -> transmets les load/unload to bank
		- d'ajouter / enlever des capacities à un capable
		- de transformer facilement un capable en corpse par exemple
		- [x] il doit pouvoir spawn des entités :
			- dupliquer [CapableData] depuis une base (exemple : zombo)
			- assigner une id unique à cette nouvelle [Data]
			- ajouter cette new data à sa liste de toutes les data
			- load le capable correspondant à cette data
			- call [OnCapableSpawned(entity,spawner)] pour remonter l'info au [[RoomSystem]]

- ## 2. [CapableBank]
	- [x] la bank doit gérer le pooling + load / unloading des capables.
	- sa principale complexité est de gérer les DIFFERENTS types de capables et donc d'avoir :
		- soit une pool par type de capable
			- -> en fait on est obligé d'avoir ça pcq sinon faut detacher / attacher les scripts [Capable] aux [GameObject] qu'on load/unload bref ça prend bcp de temps donc c pas fou, vaut mieux avoir une pool pour chaque kind !
			- mais ça change rien au fait que **body/feet/inventory/animplayer** vont être des [Capacity] plus tard !
			- 
		- ~~soit une pool de capable + plusieurs sous pool de gameObjects utiles ou non type **body**, **feet**, **inventory**, etc~~
			- ~~-> en vrai body/feet/inventory ça peut très clairement être des [[Capacity]] et donc être géré au niveau du [[CapacitySystem]]~~
				- ~~-> +2~~

- ## 3. [Capable]
	- [x] l'object doit principalement être vide, à part les method **LoadData/UnloadData/UpdateData**
	- de même stocker les refs aux différentes [[Capacity]] (l'object réel du capacity system) & animplayer ?

- ## 4. [CapableData]
	- [x] doit avoir une methode **Duplicate()**


les [[Capacity]] gèrent leur propre **data** ET leur propre **logique** au sein du [[CapacitySystem]] ce qui n'est **PAS** le même systeme que celui des capables.



---
# problèmes actuels




---
# reworks
- [ ] [[CapableSystem_Proto]]