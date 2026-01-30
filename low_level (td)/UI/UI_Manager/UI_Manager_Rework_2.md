-  version actuelle : **1.5.0b**
- tags : #ux #ui #todo

- ## **objectifs**
	- régler les problèmes de stack de même niveau d'[[UI_Pool]] qui font des bugs chelous
	- simplifier l'**UX** des menus, surtout sur le [[UI_HUD]]
	- globaliser l'utilisation d'[[UI_Window]]

- ## **TODO**
	- [ ] créer un [[UI_Chest]], [[UI_Device]] qui sont des [[UI_Pool]]
	- [ ] organiser & réunifier les différentes classes d'ui :
		- [ ] [[UI_Pool]]
		- [ ] [[UI_Window]]
		- [ ] [[UI_Slot]]
	- [ ] transformer [[UI_ItemPool]] en [[UI_Window]]
	- [ ] globaliser le système d'[[UI_Window]] partout :
		- [ ] supprimer les [[UI_Inventory]] ? le remplacer par de la glue ? inventory_linker ?
		- [ ] séparer [[UI_ItemPool]] en [[ItemPool]] + [[UI_ItemPool]]
	- [ ] revoir le [[UI_HUD]]
	- [ ] rework le [[UI_InventoryMenu]]