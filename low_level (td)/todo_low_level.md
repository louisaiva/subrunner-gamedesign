

contrairement au [[todo_high_level]], ce document a pour but de détailler le plus possible les différentes étapes dans un futur proche et ou lointain. les briques détaillées peuvent être à la fois sous forme de **Reworks**, mais aussi des random bidules oklm. chaque brique doit être la plus petite possible comme ça ça a pas l'air super dur à faire mdr



# 1.5.1 : Core update

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
	- [ ] [[SaveSystem_Proto]]
		- [ ] [[WorldBuilder_Rework_1]]


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
	- [ ] Supprimer les appels vers AddCapacity() / RemoveCapacity() mais pour ça on doit avoir un moyen d'ajouter dynamiquement des capacités ?
	- [ ] dans les coffres au **gamepad** quand on click sur un [[UI_ItemStack]] avec plusieurs items (quantity > 1) ça sélectionne ensuite un autre ui_item stack au lieu de rester sur le même
	- [x] mettre "material/objects" en material par défaut si on trouve pas
	- [x] ShadowCaster2D décalé sur les portes dans les builds


# 1.5.2 : UI inventory rework

- ### Inventory rework
	- [x] [[Inventory_Rework_1]]
- ### UI rework
	- [ ] [[UI_Manager_Rework_2]]
	- [ ] supprimer [[ItemManager]] et le remplacer par un nouveau script qui est mieux et surtout ENTIEREMENT VISUEL et sur le hud
	- [ ] faire un nouveau **HUD** avec les nouveaux sprites de barre de vie/xp, "hotbar" etc
- ### File
	- [ ] faire des [[File]] des [[Item]]
	- [ ] faire des sprites de slots pour les [[File]]
	- [ ] 




# A TRIER

- [ ] réflechir mouse dynamic orientation [[2026_05_03]]

- [ ] faire un post it system quickly (ui_pool) notamment pour le qg avec une liste des courses :
	- pastas (last packet) !! important
	- 2 piles AAAAAAAA
	- 16 Yo micro sd card


- [ ] [[CapableSystem_Rework_2]]
- [ ] transformer Movable en MoveCapacity

- [ ] est-ce qu'on peut faire que le bg devient rouge quand on se fait hacker/on prend des dégats

- [ ] implement cinematics system
	- [ ] make 2 start cinematic
	- [ ] make demo completed cinematic

- [ ] implement enemy wave system for the spawners to not appear
- [ ] implement first computer UI to have a proper way to steal the door' key
- [ ] change [[UI_File]] visuals to have better UX for
	- [ ] [[UI_ExploitSelector]]
	- [ ] [[UI_Device]]
	- [ ] [[UI_HDD]]
