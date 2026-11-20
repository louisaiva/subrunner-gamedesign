	

contrairement au [[todo_high_level]], ce document a pour but de détailler le plus possible les différentes étapes dans un futur proche et ou lointain. les briques détaillées peuvent être à la fois sous forme de **Reworks**, mais aussi des random bidules oklm. chaque brique doit être la plus petite possible comme ça ça a pas l'air super dur à faire mdr



# [x] 1.5.0x : Core update

- ## Core
	- [x] [[RoomSystem_Proto]]
	- [x] [[RoomSystem_Rework_1]]
	- [x] [[CapableSystem_Proto]]
		- [x] plus de body colliders ???
	- [x] [[MotorSystem_Proto]]
	- [x] [[MotorSystem_Rework_1]]
	- [x] [[CapacitySystem_Proto]]
	- [x] [[CapableSystem_Rework_1]]
	- [x] [[CapacitySystem_Rework_1]]
	- [x] [[LevelSystem_Proto]]
	- [x] [[LevelSystem_Rework_1]]
	- [x] [[DoorSystem_Proto]]
	- [x] [[WorldBuilder_Rework_1]]
	- [x] [[WorldBuilder_Rework_2]]


- ## Capacities to rework in Data
	- [x] transformer Being en HealthCapacity
	- [x] WalkCapacity + RunCapacity (save the data pcq pour le moment ça garde l'ancienne valeur de walk_speed ce qui peut faire avancer des mobs sans moteur)
	- [x] les AnimLayer ont l'air de faire des trucs chelou sur les [Corpse] et même des fois sur des devs qui marchent random, ptet que y'a un layer qui n'a pas été enlevé et qui donc garde son ancienne fonction ce qui n'est pas ouf.
		- [x] on dirait ça reinstancie des anim layers alors que y'en a déjà des présents !

- ## Optimisations
	- [x] comprendre d'où vient la chute de fps de 1 frame au changement de room du perso
		- [x] lister potentielles raisons :
			- trop de rooms chargées d'un coup
			- [x] tilemaps de rooms trop lentes (+4)
			- trop de capables d'un coup
				- ou trop d'inventaires/layers/colliders à load ?
			- trop de capacités d'un coup
				- > si c le cas on peut par exemple delay certaines capacités qu'on a pas besoin immédiatement
			- GC Alloc ?



- ## Autres
	- [x] faire que ça build mdr -> on lance tous les logs et on build puis on inspecte
	- [x] [[MovableEngine]] HalfMatrix stills some bugs when resizing the matrix oh no

	- [x] mettre "material/objects" en material par défaut si on trouve pas
	- [x] ShadowCaster2D décalé sur les portes dans les builds


# [x] 1.5.1x : 4th july Demo

- demo finale:
	- [x] [[july26demo]]

- ## Core
	- [x] [[Controller_Rework_1]]
	- [x] [[SaveSystem_Proto]]
	- [x] [[StorySystem]]
	- [x] [[EcoSystem_Proto]]
	- [x] [[Pasta Crafting System]]
	- [x] (~) bug drop item avec HoverBasedInteractCapacity

- ## Core bugs

	- [x] bug de [[HealthCapacity]] : quand un capable meurt des fois ça marche pas ? ça l'unload pas dans le [[CapableSystem]] ????

	- [x] [[ControllerSystem]] + [STATIC Save]
		- [x] quand on translate le [Level] dans le [[WorldBuilder]] ça fait regrab les capables par les chunks avant de **DESTROY** les capables, ce qui peut entraîner le **ControlleurDestroy** et surtout supprimer le capable controllé et aussi ses fichiers de save !!! parce que [bob-1] n'est plus dans les fichiers !
			- >  (y'a une protection en fait déjà sur ce controlleur destroy risk, mais pas sur la destruction de fichiers)
			- [x] > protéger aussi bob et le ramener à 0,0 en cas de suppression des fichiers esquivée.

	- [x] [[ControllerSystem]]
		- [x] ghost / skins on perso not working
	- [x] [[ControllerSystem]] : fix health callbacks issue
		- [x] fix perso respawn on death, on sofa
		- [x] this is the issue : ![[image-21.png]]

	- [x] fix sofa issue, on doit pouvoir en sortir n'importe quand, pas seulement via le UI_Pool. autoriser les inputs du perso

	- [x] [[DoorSystem]] rework : [[DoorSystem_Rework_1]]
	- [x] Doors :
		- [x] verticales : mettre seulement la position de l'IF au milieu c'est chouette comme ça
		- [x] le layer mid est malheuresement passé sur du ceiling, à remettre
		- ~~[x] faire qu'elles se ferment automatiquement au bout de x secondes~~

- ## Gamepad
	- [x] [[UI_PopupPool]] bug quand on appuie direct sur entrée avec que du vide ça valide aps
	- [x] pareil au gamepad quand on appuie sur A
		- > virer tout simplement les "enter world name" pour la démo
	- [x] dans les coffres au **gamepad** quand on click sur un [[UI_ItemStack]] avec plusieurs items (quantity > 1) ça sélectionne ensuite un autre ui_item stack au lieu de rester sur le même

- ## Small bugs
	- [x] Supprimer les appels vers AddCapacity() / RemoveCapacity() mais pour ça on doit avoir un moyen d'ajouter dynamiquement des capacités ?
	- [x] drop cassé dans [[UI_ChestPool]] ça drop sur le sol au lieu de le mettre dans le coffre ?
	- [x] UI_OutlineSlot ne grab que la moitié du stack

	- [x] ### UI
		- [x] mettre des croix top right pour sortir de :
			- [x] [[UI_InventoryMenu]]
			- [x] [[UI_ChestPool]]
		- [x] supprimer les [SwitchToHUD()] et tout remplacer par des [UnstackPool()] : settings, 

	- [x] mettre des colliders feet pour les tags avec layer "SemiGhost" ? comme ça les rooms grabbent sur ce layer aussi

	- [x] items qui viennent d'etre drop ont pas encore de [GetRealRoom()] parce qu'ils viennent de passer de free à pas free donc on peut pas regrab direct malheuresement ://

# [x] 1.5.2x : UI inventory rework

- ### Inventory rework
	- [x] [[Inventory_Rework_1]]
- ### UI rework
	- [x] supprimer [[ItemManager]] et le remplacer par un nouveau script qui est mieux et surtout ENTIEREMENT VISUEL et sur le hud
	- [x] faire un nouveau **HUD** avec les nouveaux sprites de barre de vie/xp, "hotbar" etc
	- [x] faire que le [[WorldSelector]] soit accessible manette
# [ ] 1.5.3x : Core Preparation

- ### Finish COre design
	- [ ] design [[CapableSystem_Rework_3]]
	- [ ] design [[CapableSystem_Rework_4]]
	- [ ] design [[ChunkSystem_Rework_3]]
	- [ ] design [[AnimSystem_Rework_1]]

- ### UI / QOL
	- [ ] check input at awake of title screen. it gets stuck with mouse even tho it receives gamepad input ?




# A TRIER


- [ ] fix divers bugs des [[july26demo]]/[[oct26demo]] : 
	- [ ] [[2026_09_22]]
	- [x] [[2026_09_28]]


- [ ] level design ? objects ?
	- [ ] > mettre des objets interactifs qui ouvre un [[UI_Pool]] en particulier par exemple un placard qui affiche l'inventaire (ou miroir) tuto + récompense le joueur pour l'exploration
	- [x] faire un post it system quickly (ui_pool) notamment pour le qg avec une liste des courses :
		- pastas (last packet) !! important
		- 2 piles AAAAAAAA
		- 16 Yo micro sd card


- [ ] ui :
	- [ ] mettre un bouton save and exit dans le [[UI_PauseMenu]] quand **dev_tools** est à 0, les deux boutons de d'hab sinon
	- [x] UI hover pas assez visible

	- [ ] rework le [[UI_Sofa]] :
		- [ ] mettre des boutons, un pour save la partie, un pour regarder la télé (qui devient eteindre la télé une fois appuyé)
		- [ ] lorsqu'on appuie sur la télé, ça allume la télé et donc ça stacke le **UI_TV** par dessus le canap.
			- [x] pour empecher de slide à gauche à droite dans le UI_Sofa (et donc perdre les boutons quand la télé est eteinte), on doit simplement désactiver les UI_Slot de la pool UI_TV donc y'a pas d eproblème en fait ça se fait automatiquement

	- [ ] rework le [[UI_TV]]:
		- [ ] faire un écran de TV fullscreen avec que les bords de la télé et au milieu un shader qui applique un effet retro télé, avec peut etre le TV screen subrunner title au milieu ?
		- [ ] ensuite si on va à droite ou à gauche on zappe les chaines de la télé
			  --> **UI_PanelManager**
		- [ ] comme ça on peut avoir une animation quand on arrive sur le canap et qu'on allume la télé où on voit nos coeurs se recharger, un texte qui écrit **world saved** en ligne de commandes cmd

		- [ ] en même temps essayer de faire bien la size & le format
			- [ ] faire une classe [Screen] qui contient plusieurs methodes **static** qui facilitent la vie :
				- [ ] connaitre la world position au milieu de l'écran
				- [ ] connaitre la canvas position au milieu de l'écran
		- [x] déjà réduire l'alpha global des slots normal & disabled
		- [ ] quand on hover qqch, tous les autres UI_ItemStack perdent de l'alpha
	- [x] faire que quand on maintient la touche pour basculer des items d'un slottable à l'autre ça s'arrete lorsque tous les items sont dans l'autre ui.
		- [x] > ça navigue quand même vers l'autre ui mais ça annule le drop continu. si on relache et qu'on remaintient par contre ça relance
		- [ ] [edge-case] encore un léger bug edge case au niveau du moving ui item, des fois dcp ça prevent le prochain drop release, ce qui annule l'effet du ui moving drop, peut etre voir ça après ?
	- [ ] > [mid-term] reprendre la même logique que le changement de UI_Slottable qui cancel l'**endless drop**, mais avec le **endless navigate**, seulement pour certains slottables / UI_Pool ? genre sur l'écran titre on veut pouvoir confirmer qu'on veut aller dans les options de customization

	- [ ] est-ce qu'on peut faire que le bg devient rouge quand on se fait hacker/on prend des dégats

	- [ ] implement first computer UI to have a proper way to steal the door' key



- [ ] ### File
	- [ ] faire des [[File]] des [[Item]]
	- [ ] corriger les derniers bar de [UI_ItemBar]	
	- [x] faire des sprites de slots pour les [[File]]
	- [ ] change [[UI_File]] visuals to have better UX for
		- [ ] [[UI_ExploitSelector]]
		- [ ] [[UI_Device]]
		- [ ] [[UI_HDD]]


- [ ] **speed run techniques**
	- [ ] dodge quand on passe à travers une porte nous donne un gain de vitesse
	- [ ] sur un spawner aussi ?
	- [ ] faire qu'il y ait une fenetre de gain de vitesse possible à chaque dodge au milieu du dodge
		- [ ] et la porte détecte quand le joueur franchit précisément la porte, et si c dans la fenetre de temps, alors ça "prolonge" le dodge


# DEPRECATED ???

- [ ] [long-term] transformer Movable en MoveCapacity

- [ ] [[CapableSystem_Rework_2]]
- [ ] [[UI_Manager_Rework_2]]