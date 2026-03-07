- #rework #done 

- version actuelle : **1.5.0**

- ## **objectifs**
	- réunifier le système d'inventaire car il part dans tous les sens (UI_ItemPool, UI_Inventory, UI_QuickItemPool, UI_Slottable etc, UI_Windows)
	- la réunification doit se faire échelle par échelle :
		- on réunit tous les UI_ItemPool/UI_Inventory etc (les slottables en gros) sous la forme UI_Slottable
		- on réunit tous les slots sous la forme UI_Slot
	- supprimer les scripts qui ne servent à rien
	- faire que la logique soit complètement indépendante de l'ui. L'ui, quant à lui, est complètement dépendant de la logique.

- ## **TODO**

	- [x] faire que [[Inventory]] ne repose plus sur l'[[UI_Inventory]] (qui ne devrait plus exister d'ailleurs) mais se repose sur des [[ItemPool]]
	- [x] enlever les bugs de [[LaptopInventory]] & [[PlacerInventory]] pour continuer à rework
	- [x] faire que c'est [[ItemPool]] qui s'occupe de mettre le bon parent etc aux items
			- ----->  [[UI_Manager_Rework_2]] ?

	- [x] séparer [[UI_ItemPool]] en [[ItemPool]] + [[UI_ItemPool]]
		- [x] les élements d'UI n'ont donc plus d'**ItemRule**, mais par contre chaque UI_ItemPool est associé à une ItemPool et peut donc accéder à l'itemrule du ItemPool
	- [x] Connecter [[UI_ItemPool]] à [[ItemPool]] pour afficher les items de la pool
	- [x] comment on gère l'assignage dynamic des [[ItemPool]] avec leurs equivalents [[UI_ItemPool]] ?
		- [x] [[Controller]] assigne les différents **ItemPool** de l'inventaire aux **UI_ItemPool** respectifs, ainsi quand on change de capable controllé bah ça change aussi les pools de l'inventaire ?

	- [x] fixer la hiérarchie de l'[[UI_InventoryMenu]] :
		- [x] virer [[UI_Laptop]]
		- [x] enlever le [[UI_Panel]] des **shortcuts** et leur assigner 4 [[UI_ItemPool]]
		- [x] enlever le **singleton** de [[UI_LaptopItemSlot]] et clean tous les events qui vont avec (sur le perso/controller ???)
		- [x] virer **hardware_stack** pour le moment et la remplacer par un **shoes-stack**
		- [x] repositionner tout ce beau monde ?

	- [x] clean complètement [[UI_Item]] pour que ça soit juste visuel et que ça se repose limite entièrement sur [[ItemStack]]
		- [x] revoir le changement abrupt de UI_Item c'etait ptet pas une idée super mdr
		- [x] enqueter sur keskispass quand on merge 2 ui_items, ce que ça fait au niveau de l'inventaire et de l'UI
	- [x] comprendre pourquoi les ui_items empty sont pas désactivés quand on ouvre l'inventaire menu
		- [x] on dirait que [[UI_ItemMover]] ne fonctionne pas dans ses methods disable_only_empty and enable_only_recevable ... faire des logs
			- [x] mdrrrrr le bug du turfu trop con : en gros quand on récupérait les ui_item_pools on récupérait directement les slottables du [[UI_Navigator]] et dans une boucle while on comparait des trucs et ensuite supprimait ces slottables... ce qui veut dire qu'on supprimait les slottables du navigator :| mdrrr tu m'étonnes ça marchait pas et c'était dur à debug, maintenant hop petite copie et c parf
		- [x] est-ce que la gestion du **Disable** ne devrait pas plutôt être assignée au [[ItemStack]] plutot qu'au UI_ItemStack seulement ? comme ça on pourrait gérer de manière logique les trucs pcq là c que visuel
			- --> en vrai non. le disable n'est que pour echanger des items de pool dans l'ui, donc c'est que visuel, pas besoin de le mettre sur item stack

	- [x] faire que les [[UI_Inventory]] n'aient plus aucune utilité
	- [x] puis les transformer en **ui** d'inventory directement, héritée de [[UI_ItemPool]] mais qui affiche pas une ItemPool mais un Inventory complet (avec une item rule d'affichage)
		- [x] régler les problèmes de drop /!\ on dirait que le [[GamepadNavigator]] cause des problèmes ?
		- [x] bug quand on move depuis un [[UI_CompactItemPool]] vers un item stack (même qui a une pool valide) bah ça marche pas pcq on peut pas accéder au ItemPool -> fixed with checking inside ui_itemmover
	- [x] créer un [[UI_Slot]] spécifique qui permet de récupérer les items qu'on dépose dans un [[UI_CompactItemPool]] un truc global qui prend toute la place du CanvasGroup
		- [x] régler les problèmes de taille du slot ([[UI_AutoLayoutOnGroup]])
		- [x] associer les sprites & marges qui vont bieng
		- [x] faire que quand on drop qq chose dedans ça marche bien
		- [x] régler soucis avec le [[GamepadNavigator]]
			- [x] faire que le slot ne peut etre choisi en closest slot (!) seulement quand on demande manuellement au navigator, pcq pour le moment on peut tout simplement jamais y naviguer
			- [x] fix les bugs de [[UIC (UI_InputsController)]] in-game qui fait qu'un appui sur A déclenche à la fois le activate & le drop
				- -> on peut simplement supprimer le activate ingame ?
	- [x] [[UI_CompactItemPool]] fixes :
		- [x] fix bug pas suppresion des itemstacks lors du detach