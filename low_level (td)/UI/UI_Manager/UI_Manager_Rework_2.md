#ux #ui #todo

- version actuelle : **1.5.0b**

---

- ## **objectifs**
	- régler les problèmes de stack de même niveau d'[[UI_Pool]] qui font des bugs chelous
	- simplifier l'**UX** des menus, surtout sur le [[UI_HUD]]
	- globaliser l'utilisation d'[[UI_Window]]

---

- ## **TODO**
	- [ ] créer/rework des [[UI_Pool]]
		- [x] un [[UI_ChestPool]]
		- [ ] de même [[UI_Device]]
		- [ ] revoir le [[UI_HUD]]
		- [x] rework le [[UI_InventoryMenu]]
	- [ ] organiser & réunifier les différentes classes d'ui :
		- [ ] [[UI_Pool]]
		- [ ] [[UI_Window]]
		- [ ] [[UI_Slot]]
	- [ ] transformer [[UI_ItemPool]] en [[UI_Window]]

	- [ ] [[ItemManager]] relink to [[ItemPool]] ? on a vraiment besoin d'ItemManager ?
		- [x] la récupération des bons items se fait désormais directement depuis l'**Inventory** dcp PIC récupère les usables directement là
		- [ ] supprimer ItemManager et le remplacer par un **UI_ItemBarHUD** ??
			- > OUI (+3)