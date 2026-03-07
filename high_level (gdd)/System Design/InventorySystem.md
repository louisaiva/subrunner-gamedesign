#system #designing


---

# description

**InventorySystem** est le système qui s'occupe de la gestion logique des [[Item]] appartenant à chaque [[Capable]] au sein d'un [[Inventory]]

Ce système est purement logique (pas de graphismes), mais il est étroitement lié avec l'**UISystem** de [[UI_Manager]], étant donné qu'une des missions principales de l'ui est d'organiser la gestion des items dans des coffres etc etc et permettre au joueur d'intéragir avec les différents inventaires.

Malgré ce lien étroit, **InventorySystem** peut totalement fonctionner en standalone, sans [[UI_Manager]]. L'inverse cependant est faux. On dit que l'UI s'appuie sur l'InventorySystem, tandis que l'inventaire est indépendant de l'ui

---

# fonctionnement du système

chaque [[Capable]] possède un [[Inventory]]. Cet inventaire possède plusieurs [[ItemPool]], qui stockent à leur tour des [[ItemStack]] qui enfin stockent des [[Item]].

Lorsqu'un capable s'approche d'un item et le grab, voici ce qu'il se passe :
- **Inventory.Grab(item)** est appelée
	- elle appelle dans une loop tous les **ItemPool.Grab(item)** pour vérifier qu'une itempool peut grab
		- elle verifie que l'item est pas nul
		- qu'il valide son **item rule**
		- elle parcourt ses ItemStack et essaie de mettre l'item dedans
	- si on a grab, alors on déclenche **Inventory.OnItemGrabbed** 

---
# problèmes actuels

- [bug] quand on drag un stack de pommes (qty=8) d'un coffre vers l'inventaire du perso (donc on a un [[UI_CompactItemPool]] + [[UI_OutlineSlot]]) bah ça grab seulement la moitié du stack ????

---
# reworks

- [x] [[Inventory_Rework_1]]
