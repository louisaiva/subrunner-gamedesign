

contrairement au [[todo_high_level]], ce document a pour but de détailler le plus possible les différentes étapes dans un futur proche et ou lointain. les briques détaillées peuvent être à la fois sous forme de **Reworks**, mais aussi des random bidules oklm. chaque brique doit être la plus petite possible comme ça ça a pas l'air super dur à faire mdr



# 1.5.1 : Core update

- ## Core
	- [x] [[RoomSystem_Proto]]
	- [x] [[RoomSystem_Rework_1]]
	- [x] [[CapableSystem_Proto]]
		- [x] plus de body colliders ???
	- [ ] [[MotorSystem_Proto]]
	- [x] [[CapacitySystem_Proto]]
	- [ ] [[CapacitySystem_Rework_1]]
	- [x] [[CapableSystem_Rework_1]]
	- [x] [[LevelSystem_Proto]]
	- [ ] [[WorldSystem_Proto]]
	- [ ] [[LevelSystem_Rework_1]]
- 
- ## Capacities to rework in Data
	- [x] transformer Being en HealthCapacity
	- [ ] WalkCapacity + RunCapacity (save the data pcq pour le moment ça garde l'ancienne valeur de walk_speed ce qui peut faire avancer des mobs sans moteur)

- ## Autres
	- [x] faire que ça build mdr -> on lance tous les logs et on build puis on inspecte
	- [x] [[MovableEngine]] HalfMatrix stills some bugs when resizing the matrix oh no
	- [ ] Supprimer les appels vers AddCapacity() / RemoveCapacity() mais pour ça on doit avoir un moyen d'ajouter dynamiquement des capacités ?


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
