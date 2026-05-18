#rework #todo

-  version de création : **1.5.0t**
-  version de résolution : 

---
- ## **objectifs**

	- étendre la modularité apportée par le [[CapacitySystem]] aux systèmes intégrés dans la [CapableData], notamment :
		- [[AnimPlayer]] & [[AnimLayer]]
		- [[Inventory]]
	- 
	- alléger la capable data
	- améliore l'intégration au [[SaveSystem]] dans le même temps




---
- ## **TODO**


	- [ ] faire une [[AnimCapacity]] qui fait le lien entre le [[Capable]] & [[AnimPlayer]]
		- ? est-ce que les files ont vraiment besoin d'animcapacity ?
		- [ ] y garder une variable [skin] template un peu en gros !
		- [ ] gère la data
		- [ ] merge [AnimPlayerData] en une seule AnimData ?

	- [ ] faire une [[InventoryCapacity]] qui relie à l'inventaire
		- certains capables n'ont pas besoin d'inventaire donc c nickel